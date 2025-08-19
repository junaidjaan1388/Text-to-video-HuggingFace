def enhance_prompt(prompt: str, style: str, lighting: str, aspect_ratio: str):
    styles = {
        "realistic": "photorealistic, ultra-detailed, cinematic lighting, 8K resolution",
        "anime": "anime style, Studio Ghibli, vibrant colors, cel-shaded",
        "painting": "oil painting style, visible brush strokes, artistic composition",
        "cyberpunk": "cyberpunk 2077 style, neon lights, futuristic cityscape"
    }
    
    lighting_options = {
        "natural": "natural daylight, soft shadows, golden hour lighting",
        "soft": "soft diffused lighting, gentle shadows, studio quality",
        "dramatic": "dramatic chiaroscuro lighting, high contrast, cinematic",
        "studio": "professional studio lighting, clean highlights, shadowless"
    }
    
    aspect_ratios = {
        "16:9": "wide angle landscape, cinematic 16:9 aspect ratio",
        "9:16": "vertical composition, 9:16 aspect ratio for mobile",
        "1:1": "square format, centered composition, Instagram style",
        "4:3": "classic television aspect ratio, retro 4:3 format"
    }
    
    enhancements = [
        styles.get(style, ""),
        lighting_options.get(lighting, ""),
        aspect_ratios.get(aspect_ratio, ""),
        "trending on ArtStation, Unreal Engine 5 render",
        "high quality, 4K resolution, professional photography"
    ]
    
    return f"{prompt}, {', '.join([e for e in enhancements if e])}"