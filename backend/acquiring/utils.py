import requests
from django.conf import settings


def send_payment_email(recipient_email, message):
    """Sending message via Unisender method."""
    url = settings.DEFAULT_CONF["base_url"]

    data = {
        "api_key": settings.DEFAULT_CONF["api_key"],
        "format": "json",
        "email": recipient_email,
        "sender_email": settings.DEFAULT_FROM_EMAIL,
        "sender_name": settings.UNISENDER_SENDER_NAME,
        "subject": "Payment information",
        "body": message,
        "list_id": 1,
    }

    response = requests.post(url, data=data)

    if response.status_code != 200:
        print(f"Ошибка при отправке сообщения: {response.status_code}")
    # TODO: добавить содержимое ответа для дополнительной информации об ошибке
    else:
        print("Сообщение успешно отправлено")


# TODO: добавить логику для обработки подтверждения
#  от UniSender о фактической отправке сообщения
