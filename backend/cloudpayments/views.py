import datetime
import requests

from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .models import CloudPayment
from .serializers import CloudpaymentsSerializer


class CloudPaymentsViewSet(ViewSet):
    """
    Вьсюсет для Cloudpayment.
    """

    def create(self, request):
        """
        Создание экзепмляра Cloudpayment.
        """
        amount = request.data.get("amount")
        url = "https://api.cloudpayments.ru/payments/tokens/create"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {settings.CLOUDPAYMENTS_PUBLIC_KEY}:"
                             f"{settings.CLOUDPAYMENTS_SECRET_KEY}"
        }
        data = {
            "Amount": amount,
            "Currency": "RUB",
            "AccountId": settings.CLOUDPAYMENTS_ACCOUNT_ID,
            "Email": request.user.email,
            "Description": "Денежный перевод",
            "JsonData": {
                "OrderId": self.generate_unique_order_id()
            }
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            payment_token = response.json().get("Model").get("Token")
            cloudpayments_instance = CloudPayment(
                user=request.user,
                amount=amount,
                currency="RUB",
                order_id=data["JsonData"]["OrderId"],
                payment_token=payment_token
            )
            cloudpayments_instance.save()
            serializer = CloudpaymentsSerializer(cloudpayments_instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Ошибка при создании платежа"},
                            status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def generate_unique_order_id():
        """
        Создание идентификатора перевода.
        """
        return datetime.datetime.now().strftime("%Y%m%d%H%M%S")
