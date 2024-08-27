


from farcaster import warpcast

# Define the private key and FID
ACCOUNT_PRIVATE_KEY = '0x6c020b37dfa6aae9fcef20f4aa8c08ef548d329c'  # Your account key's private key
FID = 842279  # Your fid

# Create the signer instance
ed25519_signer = NobleEd25519Signer(ACCOUNT_PRIVATE_KEY)

# Define network options
data_options = {
    'fid': FID,
    'network': FarcasterNetwork.MAINNET
}

# Create the cast
cast = make_cast_add(
    {
        'text': 'This is a cast!',  # Text can be up to 320 bytes long
        'embeds': [],
        'embedsDeprecated': [],
        'mentions': [],
        'mentionsPositions': []
    },
    data_options,
    ed25519_signer
)

# Print or use the cast result
print(cast)
