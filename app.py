from flask import Flask, render_template, request, send_from_directory, redirect, Response, jsonify, session, send_file
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from presets import make_orientation, make_prompt
from PIL import Image, PngImagePlugin
from datetime import datetime
import requests
import string
import random
import base64
import io
import os

verbose = False # Prints info's about the request 
port = 7000 # Change this to the port you want this chat style ui to start
webui_url = "localhost:21128" # Change this to the A1111 webui url/port
upscaler_model = "R-ESRGAN 4x+" # Change this to the upscaler you want to use
translate = False # Enables translation of the prompt
translator_model = "Helsinki-NLP/opus-mt-de-en" # Change this to the desired language. For french use for example: Helsinki-NLP/opus-mt-fr-en

app = Flask(__name__)
characters = string.ascii_letters + string.digits

if translate:
    tokenizer = AutoTokenizer.from_pretrained(translator_model)
    model = AutoModelForSeq2SeqLM.from_pretrained(translator_model)

def imagegen(sd_prompt, orientation, style, ip):
    global translate
    global webui_url
    global verbose
    tiling = False
    currentTime = datetime.now()
    if translate:
        input_ids = tokenizer.encode(sd_prompt, return_tensors="pt")
        translate = model.generate(input_ids=input_ids, max_length=512, num_beams=2, early_stopping=True)
        translated_prompt = tokenizer.decode(translate[0], skip_special_tokens=True)
    else:
        translated_prompt = sd_prompt 
    if verbose:
        print("\nPrompt:", sd_prompt, "\nAusrichtung:", orientation, "\nStyle:", style, "\nIP:", ip, "\nTime:", currentTime.strftime("%H:%M:%S", "\nTranslated Prompt:", translated_prompt))     
        
    width, height, upscale, steps = make_orientation(orientation)
    prompt, negativeprompt = make_prompt(translated_prompt, style)       

    payload = {
        "prompt": prompt,
        'negative_prompt': negativeprompt,
        "steps": steps,
        'width': width,
        'height': height,
        'cfg_scale': 8,
        'sampler_name': 'Euler',
        'seed': -1,
        'tiling': tiling,
        'restore_faces': True
    }

    response = requests.post(url=f'{webui_url}/sdapi/v1/txt2img', json=payload)
    r = response.json()
    
    for i in r['images']:
        image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))
        
        png_payload = {
            "image": "data:image/png;base64," + i
        }
        response2 = requests.post(url=f'{webui_url}/sdapi/v1/png-info', json=png_payload)
    
        pnginfo = PngImagePlugin.PngInfo()
        pnginfo.add_text("parameters", response2.json().get("info"))
        global upscaler_model
        if upscale:
            upscale_payload = {
              "upscaling_resize_w": 1500,
              "upscaling_resize_h": 1500,
              "upscaling_crop": True,
              "upscaler_1": upscaler_model,
              "image": i
            }
            
            response_upscaled = requests.post(url=f'{webui_url}/sdapi/v1/extra-single-image', json=upscale_payload)
            r_u = response_upscaled.json()
            image_bytes = base64.b64decode(r_u['image'])
            image = Image.open(io.BytesIO(image_bytes))
            
        global characters
        random_string = ''.join(random.choice(characters) for i in range(24))
        file_path = f"GeneratedImages/{random_string}.png"
        image.save(file_path, pnginfo=pnginfo)
        if verbose:
            print ("Generated Image:", request.host_url + file_path)
        return f"{request.host_url}{file_path}"

@app.route('/GeneratedImages/<path:path>')
def send_generated_image(path):
    return send_from_directory('GeneratedImages', path)
                
@app.route("/")
def assistant_image():
    return render_template("index.html", charset="utf-8")

@app.route("/getimage")
def get_image_response():
    user_text = request.args.get("msg")
    style = request.args.get("style")
    orientation = request.args.get("format")
    ip = request.remote_addr
    botresponse = imagegen(user_text, orientation, style, ip)
    return str(botresponse)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, port=port)