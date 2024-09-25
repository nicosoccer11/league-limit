import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv('API_KEY')

if not API_KEY:
    api_key = input("Please enter your API key: ")
    with open(".env", "w") as f:
        f.write(f"API_KEY={api_key}\n")