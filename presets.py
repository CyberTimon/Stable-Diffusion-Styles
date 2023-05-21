def make_orientation(orientation):
    if '2' in orientation:
        width = 768
        height = 512
        upscale = True
        steps = 25
    elif '3' in orientation:
        width = 512
        height = 768
        upscale = True
        steps = 25
    elif '1' in orientation:
        width = 512
        height = 512
        upscale = False
        steps = 20
    elif '4' in orientation:
        width = 640
        height = 640
        upscale = True
        steps = 25
    else:
        width = 512
        height = 512
        upscale = False
        steps = 20
    return width, height, upscale, steps
    
def make_prompt(prompt, style):
    if style == 'no_style':
        preprompt = ""
        afterprompt = ""
        negativeprompt = "Bad, low quality, worst quality, ugly, old, watermarks, text, signature"
    elif style == 'lowpoly':
        preprompt = "A low poly image of a " 
        afterprompt = ", low poly, soft lighting, cute, masterpiece, (best quality), polygon, trending on artstation, sharp focus, low poly model, render, 4k, flat colors"
        negativeprompt = "Bad, low quality, worst quality, ugly, old, realistic, watermarks, text, signature"
    elif style == 'anime':
        preprompt = "An picture of a "
        afterprompt = ", anime style, masterpiece, (best quality), fantasy, trending on artstation, anime-style, bokeh, dreamlike, concept art, hyperrealism, color digital painting, anime aesthetic, cinematic lighting, gapmoe kuudere trending pixiv, by greg rutkowski makoto shinkai takashi takeuchi studio ghibli"
        negativeprompt = "Bad, low quality, worst quality, ugly, old, deformed iris, deformed pupils, out of frame, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck, raw, drops, particles, watermarks, text, signature"
    elif style == 'oilpainting':
        preprompt = "Oil painting of a "
        afterprompt = ", oil painting, colors, art, ink, drawing, oil brushstrokes, abstract, paint textures, by Leonid Afremov"
        negativeprompt = "Bad, low quality, worst quality, ugly, old, nsfw, watermarks, text, signature"
    elif style == 'cute':
        preprompt = "Cute image of a "
        afterprompt = ", fantasy, miniature, soft lighting, flat colors, dreamlike, small, surrealism, bokeh, unreal engine, trending on artstation"
        negativeprompt = "Bad, low quality, worst quality, ugly, old, realistic, dark, reallife, texture, realistic, raw"
    elif style == 'comic':
        preprompt = "Comic image of a "
        afterprompt = ", comic, anime style, 1970 magazine, illustration"
        negativeprompt = "Bad, low quality, worst quality, ugly, old, realistic, raw, watermarks, text, signature"
    elif style == 'cyberpunk':
        preprompt = "A picture a "
        afterprompt = ", futuristic, lights, high quality, cyberpunk, greg rutkowski, highly detailed, trending on artstation, michal lisowski"
        negativeprompt = "Bad, low quality, worst quality, ugly, old, human, watermarks, text, signature"
    elif style == 'steampunk':
        preprompt = "A digital illustration of a steampunk a "
        afterprompt = ", clockwork machines, 4k, detailed, trending in artstation, mechanism, metal, pipes, fantasy vivid colors, sharp focus"
        negativeprompt = "Bad, low quality, worst quality, ugly, old, realistic, raw, human, watermarks, text, signature"
    elif style == 'vintage':
        preprompt = "Vintage 1950s illustration poster of a "
        afterprompt = ", low contrast, vintage, 1950, old fashion, illustration, vector, flat colors, flat design"
        negativeprompt = "ugly, realistic, raw, text, title, colorful, description, watermarks, text, signature"
    elif style == 'apocalyptic':
        preprompt = "A apocalyptic picture of a "
        afterprompt = ", distopic, cinestill, photography, scary, foggy, ruin, realistic, hyper detailed, unreal engine, cinematic, octane render, lights, greg rutkowski"
        negativeprompt = "ugly, realistic, raw, text, title, colorful, description, watermarks, text, signature"
    elif style == 'natural':
        preprompt = "RAW photo of a "
        afterprompt = ", dslr, soft lighting, high quality, hdr, Fujifilm XT3"
        negativeprompt = "(deformed iris, deformed pupils, semi-realistic, dark-skinned, cgi, 3d, render, sketch, cartoon, drawing, anime:1.4), text, close up, cropped, out of frame, worst quality, low quality, jpeg artifacts, bokeh, ugly, duplicate, fat, old, aged, fat, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, nude, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, black, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck, watermarks, text, signature"
    elif style == 'watercolor':
        preprompt = "A watercolor painting of a "
        afterprompt = ", detailed line art, color explosion, ink drips, art, watercolors, wet, single color, abstract, by ilya kuvshinov"
        negativeprompt = "Bad, low quality, worst quality, ugly, old, human, woman, realistic, anime, japan, nsfw, watermarks, text, signature"
    elif style == 'cinematic':
        preprompt = "RAW cinematic picture of a "
        afterprompt = ", cinematic look, cinematic, best quality, 70mm lens, lightroom, Nikon Z FX, sharp focus, Fujifilm XT3, (rutkowski:1.1), artstation, HDR, greg rutkowski"
        negativeprompt = "(deformed iris, deformed pupils, semi-realistic, dark-skinned, cgi, 3d, render, sketch, cartoon, drawing, anime:1.4), text, close up, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate, fat, old, aged, fat, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, nude, mutation, nsfw, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, black, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck, watermarks, text, signature"
    elif style == 'tiling':
        preprompt = ""
        afterprompt = ""
        negativeprompt = "Bad, low quality, worst quality, watermarks, text, signature"
        tiling = True
    else:
        preprompt = ""
        afterprompt = ""
        negativeprompt = "Bad, low quality, worst quality, ugly, old, watermarks, text, signature"
    prompt = preprompt + prompt + afterprompt
    return prompt, negativeprompt
