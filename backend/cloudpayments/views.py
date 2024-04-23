import datetime
import requests

from django.shortcuts import render, redirect
from django.conf import settings


def generate_unique_order_id():
    """
    Создание идентификатора перевода.
    """
    return datetime.datetime.now().strftime("%Y%m%d%H%M%S")


def payment_view(request):
    """
    Представление для Cloudpayment
    """
    if request.method == "POST":
        amount = request.POST.get("amount")
        url = "https://api.cloudpayments.ru/payments/tokens/create"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {settings.CLOUDPAYMENTS_PUBLIC_KEY}:{settings.CLOUDPAYMENTS_SECRET_KEY}"
        }
        data = {
            "Amount": amount,
            "Currency": "RUB",
            "AccountId": settings.CLOUDPAYMENTS_ACCOUNT_ID,
            "Email": request.user.email,
            "Description": "Денежный перевод",
            "JsonData": {
                "OrderId": generate_unique_order_id()
            }
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            payment_token = response.json().get("Model").get("Token")
            return redirect(f"https://api.cloudpayments.ru/payments/tokens/{payment_token}")
        else:
            return render(request, "error.html", {"error": "Ошибка при создании платежа"})
    else:
        return render(request, "payment_form.html")
