# AI Video Generator with HuggingFace

## Overview
FastAPI web app that generates videos from text using HuggingFace AI models
Demonstrates AI integration, prompt engineering, and cloud deployment

## Features
- Text-to-video generation with HuggingFace models
- Prompt enhancement (style, lighting, aspect ratio)
- Simple web interface (HTML/CSS/JS)
- FastAPI backend
- Cloud deployment ready

## Model Used
cerspense/zeroscope_v2_576w (HuggingFace)
- Resolution: 576x320 pixels
- Output: MP4 videos (2-4 seconds)
- Alternative: damo-vilab/text-to-video-ms-1.7b

## Setup
1. Clone repo: git clone <repository-url>
2. Create venv: python -m venv venv
3. Activate: source venv/bin/activate (Unix) or venv\Scripts\activate (Windows)
4. Install deps: pip install -r app/requirements.txt
5. Add HuggingFace API key to app/.env: HUGGINGFACE_API_KEY=your_key_here
6. Run: uvicorn app.main:app --reload

## Deployment (Render)
1. Push to GitHub
2. Connect repo to Render
3. Build: pip install -r app/requirements.txt
4. Start: uvicorn app.main:app --host 0.0.0.0 --port 10000
5. Add HUGGINGFACE_API_KEY env var

## Project Structure
ai-video-app/
├── app/
│ ├── main.py (FastAPI app)
│ ├── client.py (HuggingFace client)
│ ├── rag.py (prompt enhancement)
│ ├── templates/ (HTML templates)
│ ├── static/ (CSS/JS files)
│ ├── videos/ (generated videos)
│ └── requirements.txt
├── .gitignore
├── README.md
└── LICENSE

## Current Implementation
✅ Placeholder mode works (no API key needed)
✅ Full workflow simulation
✅ All API endpoints functional
✅ Frontend-backend integration
✅ Ready for deployment

For real video generation:
1. Uncomment API call in client.py
2. Add valid HuggingFace API key
3. Test locally first

## Note
- Placeholder mode creates demo videos instantly
- Real API calls may take 30-60 seconds per video
- Check HuggingFace for rate limits/pricing

## License
MIT License

