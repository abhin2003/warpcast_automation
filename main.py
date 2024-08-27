import ed25519
import requests
import json

# Configuration: Replace these with your actual credentials
ACCOUNT_PRIVATE_KEY = '0x...'  # Your account's private key (replace with your actual key)
FID = 842279  # Your Farcaster ID (replace with your actual FID)
FC_NETWORK = "mainnet"  # Network type, change if necessary

def create_cast(text, private_key, fid, network="mainnet"):
    """
    Function to create a cast on Farcaster.

    Args:
    text (str): The text content of the cast.
    private_key (str): The private key of the Farcaster account (in hex format).
    fid (int): Farcaster ID of the user.
    network (str): The network to post on, default is "mainnet".
    """
    try:
        # Set up the signer with your private key
        private_key_bytes = bytes.fromhex(private_key[2:])  # Strip '0x' prefix and convert to bytes
        signing_key = ed25519.SigningKey(private_key_bytes)
        verifying_key = signing_key.get_verifying_key()

        # Create the cast data
        cast_data = {
            "text": text,
            "embeds": [],
            "embedsDeprecated": [],
            "mentions": [],
            "mentionsPositions": [],
        }

        # Prepare data options
        data_options = {
            "fid": fid,
            "network": network,
        }

        # Serialize the data to JSON
        message = json.dumps({"cast_data": cast_data, "data_options": data_options})

        # Sign the message
        signature = signing_key.sign(message.encode('utf-8')).hex()

        # Submit the cast to the Farcaster API
        response = requests.post(
            'https://api.farcaster.network/v1/casts',  # Replace with the actual endpoint
            json={"cast_data": cast_data, "data_options": data_options, "signature": signature}
        )

        if response.status_code == 200:
            print("Cast created successfully:", response.json())
        else:
            print("Error creating cast:", response.status_code, response.text)
    
    except Exception as e:
        print("An error occurred:", str(e))

# Example usage
if __name__ == "__main__":
    create_cast('Hello, Farcaster!', ACCOUNT_PRIVATE_KEY, FID)
