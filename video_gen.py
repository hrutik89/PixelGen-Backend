import requests

RUNWAY_API_KEY = "key_3d036e17f3e2b1590b8f0b71b7eb223b0c12df4dfc807180da008c53e0b7d7e8cb8f6ffeb5c81627fb51c492e31f54a9587c5b2ba997ea6d6df25b3bcaec6ce4"

def generate_video(prompt):
    url = "https://api.runwayml.com/v1/text-to-video"
    headers = {"Authorization": f"Bearer {RUNWAY_API_KEY}"}
    data = {"prompt": prompt}
    
    response = requests.post(url, json=data, headers=headers)
    return response.json().get("video_url", "No video generated")
