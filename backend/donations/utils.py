import requests
from django.conf import settings


def send_payment_email(recipient_email, message):
    sender_email = settings.DEFAULT_FROM_EMAIL
    subject = "Payment Rejected"
    sender_name = "Vasya Pupkin"
    api_key = settings.UNISENDER_API_KEY
    list_id = 1

    url = settings.UNISENDER_SENDEMAIL_URL

    data = {
        "api_key": api_key,
        "format": "json",
        "email": recipient_email,
        "sender_email": sender_email,
        "sender_name": sender_name,
        "subject": subject,
        "body": message,
        "list_id": list_id,
    }

    response = requests.post(url, data=data)

    if response.status_code != 200:
        print(f"Ошибка при отправке сообщения: {response.status_code}")
    else:
        print("Сообщение успешно отправлено")
