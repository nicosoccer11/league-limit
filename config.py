import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv('API_KEY')
SUMMONER_NAME = os.getenv('SUMMONER_NAME')
TAGLINE = os.getenv('TAGLINE')
PATH = os.getenv('PATH')
