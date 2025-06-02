import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_KEY = os.getenv('GEMINI_API_KEY', 'your-default-key')
    MAX_IMAGE_SIZE = (1024, 1024)
    TEMP_IMAGE_PATH = "temp_image.png"
    MODEL_NAME = "gemini-1.5-flash"
