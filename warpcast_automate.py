from farcaster import Warpcast
from modules.search import search_output_dictionary
import os


FID = 842279
FARCASTER_PRIVATE_KEY = "filter wear divert sick climb barrel element blue buzz response round river inject romance provide puzzle hair note art mass smoke boat helmet ticket"
client = Warpcast(fid=FID, mnemonic=FARCASTER_PRIVATE_KEY)
print(client)

# Function to get the username of the user
def get_my_username():
    user = client.get_me()
    print("Username : ", user.username)

# Function to create cast 
def create_cast(text):
    try:
        result = client.post_cast(text)
        print("Transaction Hash : ",result.cast.hash)
        print(f"Result object: {result}")

    except Exception as e:
        print(f"Error creating cast: {str(e)}")

#Function to get the followers of a user
def follow_user(fid_user):
    client.follow_user(fid_user)





# Function to recast 
def recast(cast_hash):
    client.recast(cast_hash)

# Function to like a cast
def like_cast(cast_hash):
    client.like_cast(cast_hash)

# recast('0x5c9eb3fe15f69a96ff53f10a0726dad284e3f08c')
# like('0x5c9eb3fe15f69a96ff53f10a0726dad284e3f08c')

# toly = client.get_user(198811)
# print("Toly details ", toly)

# casttolly = client.get_casts(198811)
# print("casts of tolly : ", casttolly)

def get_hash_from_file():
    with open("casthash.txt") as file:
        lines = [line.rstrip() for line in file]


#Function to get the hash of a cast of a given user(FID)
def get_user_casts(fid, limit=25):
    casts_result = client.get_casts(fid=fid, limit=limit)
    return casts_result.casts

# Function to get the casts of a given cast


def get_fid_username(username) :
    try:
        user = client.get_user_by_username(username)
        fid = user.fid
        print(f"The FID for user '{username}' is: {fid}")
        return fid
    except Exception as e:
        print(f"Error fetching user: {e}")




# cast_text = input("Enter your cast text : ")
# create_cast(cast_text)






def main():
    try:
        get_my_username()
        list_ids = search_output_dictionary('graph', 12)
        print(list_ids)
        for i in list_ids:
            fid_user = get_fid_username(i)
            casts = get_user_casts(fid_user, 3)
            for cast in casts:
                print(cast.hash)
                like_cast(cast.hash)
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting gracefully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()




