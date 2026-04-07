from get_access_token import get_access_token
import requests

def get_mac(chat_id):
    ACCESS_TOKEN = get_access_token(chat_id)

    HEADERS = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    URL = "https://apis.cleargrass.com/v1/apis/devices"

    response = requests.get(URL, headers=HEADERS, timeout=10)

    data = response.json()

    return data['devices'][0]['info']['mac']