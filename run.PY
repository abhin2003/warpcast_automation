import requests
import json

url = "https://api.warpcast.com/v2/casts"
api_key = "wc_secret_47e58ed528731d77ab9071e364b9fab51fc11268931ce874f719fac9_4fd525f2"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

data = {
    "text": "Hello, Farcaster! This is a test cast.",
    "embeds": []  
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("Cast created successfully!")
    print(response.json())
else:
    print(f"Failed to create cast. Status code: {response.status_code}")
    print(response.text)