from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

if api_key is None:
    raise ValueError("API_KEY not found in .env file")