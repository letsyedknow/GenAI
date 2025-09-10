import os
from dotenv import load_dotenv

load_dotenv() # loads variables from .env file into environment

class cred():
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    HF_TOKEN = os.getenv("HF_TOKEN")
    GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
