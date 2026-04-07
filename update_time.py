import requests
from get_access_token import get_access_token
from get_mac_address import get_mac
import time

def up_time(chat_id, report):
    
    ACCESS_TOKEN = get_access_token(chat_id)
    MAC = get_mac(chat_id)
    URL = "https://apis.cleargrass.com/v1/apis/devices/settings"


    HEADERS = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "mac": [MAC],
        "report_interval": report,
        "collect_interval": report,
        "timestamp": int(time.time() * 1000)
    }
    print("MAC:", MAC)
    print("TOKEN:", ACCESS_TOKEN[:10])
    response = requests.put(URL, json=payload, headers=HEADERS)

    return response.status_code, response.text