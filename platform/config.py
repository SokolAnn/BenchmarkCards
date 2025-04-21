import os

OPENAI_API_KEY = "your_openai_api_key_here"
STATIC_DIR = "static"

if not os.path.exists(STATIC_DIR):
    os.makedirs(STATIC_DIR, exist_ok=True)