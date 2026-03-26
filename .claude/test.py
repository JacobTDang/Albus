import os
import requests
import json

api_key = os.getenv("GEMINI_API_KEY")
url = f"https://generativelanguage.googleapis.com/v1beta/models?key="

resp = requests.get(url, timeout=30)
print(resp.status_code)
print(json.dumps(resp.json(), indent=2))