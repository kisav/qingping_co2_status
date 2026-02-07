import base64
import requests


def get_token(app_key_and_secret):



    headers = {
        "Authorization": f"Basic {app_key_and_secret}",
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