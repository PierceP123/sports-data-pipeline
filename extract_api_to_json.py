import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("FOOTBALL_API")
URL = os.getenv("FOOTBALL_URL")

headers = {
    "X-Auth-Token": API_KEY
}

response = requests.get(URL, headers=headers)
response.raise_for_status()

data = response.json()

output_path = "data/raw/pl_matches_25_26.json"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w", encoding="utf-8") as file_output:
    json.dump(data, file_output, indent=2)

print(f"Data saved successfully to {output_path}")
print(f"Matches: {len(data.get('matches', []))}")
