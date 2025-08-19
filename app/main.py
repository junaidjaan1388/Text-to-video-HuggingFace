from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
from pathlib import Path
import uuid

try:
    from .rag import enhance_prompt
    from .client import video_generator
except ImportError:
    from rag import enhance_prompt
    from client import video_generator


app = FastAPI(title="AI Video Generator")

# Mount static files and templates
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Ensureing videos directory exists
videos_dir = Path("app/videos")
videos_dir.mkdir(exist_ok=True)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate")
async def generate_video(
    request: Request,
    prompt: str = Form(...),
    style: str = Form(...),
    lighting: str = Form(...),
    aspect_ratio: str = Form(...)
):
    try:
        # Enhance the prompt using RAG...
        enhanced_prompt = enhance_prompt(prompt, style, lighting, aspect_ratio)
        
        # Generate video using HuggingFace
        video_filename = video_generator.generate_video(enhanced_prompt)
        
        # Return th video URL
        return JSONResponse({
            "video_url": f"/videos/{video_filename}",
            "enhanced_prompt": enhanced_prompt
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/videos/{filename}")
async def get_video(filename: str):
    video_path = videos_dir / filename
    if video_path.exists():
        return FileResponse(video_path, media_type="video/mp4")
    raise HTTPException(status_code=404, detail="Video not found")

@app.get("/player", response_class=HTMLResponse)
async def video_player(request: Request, video_url: str):
    return templates.TemplateResponse("player.html", {
        "request": request,
        "video_url": video_url
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)