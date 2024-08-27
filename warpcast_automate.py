from farcaster import Warpcast
import os


FID = 842279
FARCASTER_PRIVATE_KEY = "filter wear divert sick climb barrel element blue buzz response round river inject romance provide puzzle hair note art mass smoke boat helmet ticket"

client = Warpcast(fid=FID, mnemonic=FARCASTER_PRIVATE_KEY)
print(client)

def get_my_username():
    user = client.get_me()
    print("Username : ", user.username)

def create_cast(text):
    try:
        result = client.post_cast(text)
        print("Transaction Hash : ",result.cast.hash)
        print(f"Result object: {result}")

    except Exception as e:
        print(f"Error creating cast: {str(e)}")

def follow_user(fid_user):
    client.follow_user(fid_user)

def recast(cast_hash):
    client.recast(cast_hash)

def like(cast_hash):
    client.like_cast(cast_hash)

recast('0x5c9eb3fe15f69a96ff53f10a0726dad284e3f08c')
like('0x5c9eb3fe15f69a96ff53f10a0726dad284e3f08c')

# toly = client.get_user(198811)
# print("Toly details ", toly)

# casttolly = client.get_casts(198811)
# print("casts of tolly : ", casttolly)

with open("casthash.txt") as file:
    lines = [line.rstrip() for line in file]
get_my_username()
create_cast("Hi my name is bhoomi")


# cast_text = input("Enter your cast text : ")
# create_cast(cast_text)