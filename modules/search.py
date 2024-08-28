import re
import requests
import pandas as pd
from dotenv import load_dotenv
import os


API_KEY = "AIzaSyBKtyA7yTlgtSnrrxthJU5mvp3ZrVnQqzs"
SEARCH_ENGINE_ID = "a523e4cdce5a14354"


def clean_filename(filename):
        filename = re.sub(r'[\\/*?:"<>|]', "", filename)
        return filename

def build_payload(query, start=1, num=10, date_restrict='m1', **params):
    payload = {
        'key': API_KEY,
        'q': query,
        'cx': SEARCH_ENGINE_ID,
        'start': start,
        'num': num,
        'daterestrict': date_restrict
    }
    payload.update(params)
    return payload

def make_request(payload):
    response = requests.get('https://www.googleapis.com/customsearch/v1', params=payload)
    if response.status_code != 200:
        raise Exception("Request failed with status code: {}".format(response.status_code))
    return response.json()



# Function to get the search output as dictionary
def search_output_dictionary(query, result_total=10):
    items = []
    reminder = result_total % 10
    if reminder > 0:
        pages = (result_total // 10) + 1
    else:
        pages = result_total // 10
        
    for i in range(pages):
        if pages == i + 1 and reminder > 0:
            payload = build_payload(query, start=(i * 10) + 1, num=reminder)
        else:
            payload = build_payload(query, start=(i * 10) + 1)
        response = make_request(payload)
        items.extend(response['items'])
    
    
    titles = [item['title'] for item in items]
    for title in titles[2:]:

        print(title)


# Function to get the search result as a excel file
def search_output_excel(query, result_total=10):
    items = []
    reminder = result_total % 10
    if reminder > 0:
        pages = (result_total // 10) + 1
    else:
        pages = result_total // 10
        
    for i in range(pages):
        if pages == i + 1 and reminder > 0:
            payload = build_payload(query, start=(i * 10) + 1, num=reminder)
        else:
            payload = build_payload(query, start=(i * 10) + 1)
        response = make_request(payload)
        items.extend(response['items'])

    query_string_clean = clean_filename(query)
    df = pd.json_normalize(items)
    df.to_excel('Google Search Result_{0}.xlsx'.format(query_string_clean), index=False)






search_query = 'Bitcoin'
total_results = 40
search_output_dictionary(search_query, total_results)

