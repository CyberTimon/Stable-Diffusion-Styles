
# Stable Diffusion Styles

I always wanted to have a place, where you can easily find good stable diffusion style templates. Earlier I used lexica.art for good, diverse prompt inspiration but since they changed the model to their own, closed source "Lexica Aperture" most of the shared prompts from the gallery won't work using Stable Diffusion 1.5.

If you are here and wish a easy way to create beautiful and unique pictures using my styles, you can just clone the repo, install the dependencies and run the app.py file. This will start the simple webui and you're ready to go.

To just get the prompts for the styles, feel free to just copy them from prompts.py. 

If you like this project, feel free to give it a star.  


## Goal of this repository

I created this repository to share the greatest prompt styles I made and expand this to even more the community will find. 
Second I needed a way to create beautiful images without many buttons, sliders, numbers or very large, complicated prompts.

In addition, I made a small chat-like webui to create images and upscale with great, complex styles using simple buttons. The webui should also accept multilingual prompts, so I added an option to translate the prompt from the desired language to english using an free, small open source translation model from huggingface.

Another goal was to make it compatible with Automatic 1111's API.
I think many people already use Automatic 1111 and don't want to close or use another model directory, so I made it use A1111 as backend.

## Usage

To use this webui, clone the repo, install all the dependencies and run app.py with python.

```bash
  git clone https://github.com/CyberTimon/Stable-Diffusion-Styles
  cd Stable-Diffusion-Styles
  pip install flask transformers Pillow requests
  python3 app.py
```

Settings:

```python
verbose = False # Prints info's about the request 
port = 7000 # Change this to the port you want this chat style ui to start
webui_url = "localhost:21128" # Change this to the A1111 webui url/port
upscaler_model = "R-ESRGAN 4x+" # Change this to the upscaler you want to use
translate = False # Enables translation of the prompt
translator_model = "Helsinki-NLP/opus-mt-de-en" # Change this to the desired language. For french use for example: Helsinki-NLP/opus-mt-fr-en
```

## To Do

- Make the prompts better (Sometimes "watercolor" for example generates human faces even when not prompted so)

## Screenshots
### Settings and style selection:
<img src="https://raw.githubusercontent.com/CyberTimon/Stable-Diffusion-Styles/main/Screenshot1.png" alt="App Screenshot" width="50%">

### Example generations:
<img src="https://raw.githubusercontent.com/CyberTimon/Stable-Diffusion-Styles/main/Screenshot3.png" alt="App Screenshot" width="50%">

<img src="https://raw.githubusercontent.com/CyberTimon/Stable-Diffusion-Styles/main/Screenshot2.png" alt="App Screenshot" width="50%">
