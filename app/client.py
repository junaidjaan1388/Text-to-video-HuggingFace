import os
import time
import uuid
import requests
from pathlib import Path
from dotenv import load_dotenv

# Load nvironment variabls..
load_dotenv()

class HuggingFaceVideoGenerator:
    def __init__(self):
        self.videos_dir = Path("app/videos")
        self.videos_dir.mkdir(exist_ok=True)
        self.api_key = os.getenv("HUGGINGFACE_API_KEY")
        self.api_url = "https://api-inference.huggingface.co/models"
        
        self.model_name = "cerspense/zeroscope_v2_576w"
    
    def generate_video(self, prompt: str) -> str:
        # a Uniqe filename 
        video_id = str(uuid.uuid4())
        video_filename = f"{video_id}.mp4"
        video_path = self.videos_dir / video_filename
        
        time.sleep(3)
        
        self._create_placeholder_video(video_path, prompt)
        
        return video_filename
    
    def _create_placeholder_video(self, video_path: Path, prompt: str):
        
        with open(video_path, 'w') as f:
            f.write(f"Placeholder video for prompt: {prompt}\n")
            f.write("In a real implementation, this would be an actual video file.\n")
        
        
        static_video = self.videos_dir / "static_demo_video.mp4"
        if static_video.exists():
            with open(static_video, 'rb') as src, open(video_path, 'wb') as dst:
                dst.write(src.read())

def call_huggingface_api(prompt: str, api_key: str, model: str):
    """Actual implementation for calling HuggingFace API"""
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {"inputs": prompt}
    
    try:
        response = requests.post(
            f"https://api-inference.huggingface.co/models/{model}",
            headers=headers,
            json=payload,
            timeout=60
        )
        
        if response.status_code == 200:
            return response.content
        else:
            print(f"API Error: {response.status_code} - {response.text}")
            return None
            
    except Exception as e:
        print(f"Request failed: {e}")
        return None

video_generator = HuggingFaceVideoGenerator()
