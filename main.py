import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("KEY")
api_result = requests.get("https://camru.ca/gw2026", {"key": api_key})
print(api_result.text)