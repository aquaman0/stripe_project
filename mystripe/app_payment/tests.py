import json
import requests
from django.test import TestCase


ITEM_URL = 'http://127.0.0.1:8000/item/1'
BUY_URL = 'http://127.0.0.1:8000/buy/2'


def get_item_html(url):
    api_response = requests.get(url)
    print(api_response.text)


def get_session_id(url):
    api_response = requests.get(url)
    json_response = json.loads(api_response.text)
    print(json_response)


get_item_html(ITEM_URL)
get_session_id(BUY_URL)
