from farcaster import Warpcast
import os


ACCOUNT_PRIVATE_KEY = '0x6c020b37dfa6aae9fcef20f4aa8c08ef548d329c' 
FID = 842279


client = Warpcast(
    mnemonic=None,  
    private_key=ACCOUNT_PRIVATE_KEY,
    fid=FID,
    network="mainnet"  
)



profile = client.get_user(fid=FID)
print(profile)