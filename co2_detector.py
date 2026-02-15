import os
from dotenv import load_dotenv
import requests
import time as t
from get_access_token import get_access_token

load_dotenv()


URL = os.getenv("URL_DEVICES")


def co2_status(chat_id):

    ACCESS_TOKEN = get_access_token(chat_id)

    HEADERS = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    response = requests.get(URL, headers=HEADERS, timeout=10)

    data = response.json()
    device = data["devices"][0]
    co2_value = device["data"]["co2"]["value"]

    return co2_value


    
