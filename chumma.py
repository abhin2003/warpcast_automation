import requests
import json
from nacl.signing import SigningKey
from nacl.encoding import HexEncoder

# Your Farcaster credentials
FARCASTER_MNEMONICS = "filter wear divert sick climb barrel element blue buzz response round river inject romance provide puzzle hair note art mass smoke boat helmet ticket"
FID = 842279
FARCASTER_PRIVATE_KEY = '6c020b37dfa6aae9fcef20f4aa8c08ef548d329c'



# Convert the private key to a signing key
signing_key = SigningKey(FARCASTER_PRIVATE_KEY, encoder=HexEncoder)
public_key = signing_key.verify_key.encode(encoder=HexEncoder)

# Define the cast data
cast_data = {
    'text': 'This is a cast!',  # Text can be up to 320 bytes long
    'embeds': [],
    'embedsDeprecated': [],
    'mentions': [],
    'mentionsPositions': [],
}

# API endpoint for making a cast
api_url = "https://api.farcaster.xyz/v1/cast/add"

# Define the headers and payload
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {FARCASTER_PRIVATE_KEY}',  # Adjust according to the API requirements
}

payload = {
    'fid': FID,
    'data': cast_data,
}

# Make the request
response = requests.post(api_url, headers=headers, data=json.dumps(payload))

# Print the response
print(response.status_code)
print(response.json())
