import base64
import requests
from models import get_token



def get_access_token(chat_id):


    raw = get_token(chat_id)                 
    encoded = base64.b64encode(raw.encode()).decode()


    headers = {
        "Authorization": f"Basic {encoded}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "grant_type": "client_credentials",
        "scope": "device_full_access"
    }

    r = requests.post(
        "https://oauth.cleargrass.com/oauth2/token",
        headers=headers,
        data=data
    )

    return r.json()["access_token"]

if __name__ == "__main__":
    print(get_token())