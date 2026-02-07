import os
from dotenv import load_dotenv
import requests
import time as t
import get_access_token

load_dotenv()

APP_KEY_SECRET = os.getenv("APP_KEY_SECRET")
ACCESS_TOKEN = get_access_token.get_token(APP_KEY_SECRET)
URL = os.getenv("URL_DEVICES")
print(URL)

HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

while True:
    response = requests.get(URL, headers=HEADERS, timeout=10)

    data = response.json()
    device = data["devices"][0]
    co2_value = device["data"]["co2"]["value"]

    print("CO2:", co2_value)
    t.sleep(10)
