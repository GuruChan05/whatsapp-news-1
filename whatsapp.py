import requests

from config import (
    WHATSAPP_TOKEN,
    PHONE_NUMBER_ID,
    MY_PHONE
)


def send_whatsapp(message):

    url = (
        f"https://graph.facebook.com/v19.0/"
        f"{PHONE_NUMBER_ID}/messages"
    )

    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": MY_PHONE,
        "type": "text",
        "text": {
            "body": message
        }
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=30
    )

    print(response.status_code)
    print(response.text)