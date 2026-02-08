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

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Go up one level to the project root (sports-data-pipeline)
project_root = os.path.dirname(script_dir)

# Build the path to data/raw from project root
output_dir = os.path.join(project_root, "data", "raw")
output_path = os.path.join(output_dir, "pl_matches_25_26.json")

# Create directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Write the file
with open(output_path, "w", encoding="utf-8") as file_output:
    json.dump(data, file_output, indent=2)

print(f"Data saved successfully to {output_path}")
print(f"Matches: {len(data.get('matches', []))}")
print(f"Script directory: {script_dir}")
print(f"Project root: {project_root}")
print(f"Output path: {output_path}")