import requests
from django.conf import settings


def send_payment_email(recipient_email, message):
    """Sending message via Unisender method."""
    sender_email = settings.DEFAULT_FROM_EMAIL
    subject = "Payment information"
    sender_name = "Vasya Pupkin"  # нужно прописать в настройках
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
    # TODO: добавить содержимое ответа для дополнительной информации об ошибке
    else:
        print("Сообщение успешно отправлено")


# TODO: добавить логику для обработки подтверждения
#  от UniSender о фактической отправке сообщения
