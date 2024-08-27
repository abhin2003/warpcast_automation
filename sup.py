import requests
import json
from requests.auth import AuthBase

# Define your account private key and FID
ACCOUNT_PRIVATE_KEY = '0x6c020b37dfa6aae9fcef20f4aa8c08ef548d329c'  # Your account key's private key
FID = 842279  # Your fid

# Define the Farcaster network URL
FC_NETWORK_URL = 'https://api.farcaster.network'  # Replace with the correct API URL if different

# Define the headers
headers = {
    'Content-Type': 'application/json',
}

# Define the cast message
cast_message = {
    'text': 'This is a cast!',  # Text can be up to 320 bytes long
    'embeds': [],
    'mentions': [],
    'mentionsPositions': [],
}

# Create the cast
def create_cast():
    url = f'{FC_NETWORK_URL}/cast/add'  # Replace with the correct endpoint for adding a cast
    payload = {
        'fid': FID,
        'cast': cast_message
    }
    
    # Make the POST request
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    # Check if the request was successful
    if response.status_code == 200:
        print('Cast created successfully:', response.json())
    else:
        print('Failed to create cast:', response.status_code, response.text)

# Run the function to create a cast
create_cast()
