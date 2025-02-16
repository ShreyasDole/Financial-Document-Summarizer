import os
from dotenv import load_dotenv

# Load API Key from .env
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("Missing Google API Key! Please set it in the .env file.")
