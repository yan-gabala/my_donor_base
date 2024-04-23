import requests

from django.http import JsonResponse
from payments.core import BasicProvider

from .forms import CloudPaymentsForm


class CloudPaymentProvider(BasicProvider):
    """
    Провайдер для платежной системы Cloudprovider.
    """

    def get_form(self, payment, data=None):
        """
        Возвращает форму для оплаты.
        """
        form = CloudPaymentsForm(data)
        return form

    def process_data(self, payment, request):
        """
        Обрабатывает данные, полученные от платежной системы.
        """
        data = request.POST
        transaction_id = data.get("transaction_id")
        payment_status = data.get("payment_status")
        amount = data.get("amount")
        payment.transaction_id = transaction_id
        payment.amount = amount
        if payment_status == "success":
            payment.status = "paid"
        elif payment_status == "failure":
            payment.status = "failed"
        elif payment_status == "pending":
            payment.status = "waiting"
        payment.save()
        response_data = {
            "transaction_id": transaction_id,
            "payment_status": payment_status,
            "amount": amount
        }
        return JsonResponse(response_data)

    def capture(self, payment, amount=None):
        """
        Захватывает платеж.
        """
        capture_url = "https://api.cloudpayments.ru/payments/confirm"
        params = {
            "TransactionId": payment.transaction_id,
            "Amount": amount if amount else payment.amount
        }
        response = requests.post(capture_url, data=params)
        if response.status_code == 200:
            payment.status = "captured"
            payment.save()
            return JsonResponse({"status": "success",
                                 "message": "Оплата успешно захвачена."})
        else:
            return JsonResponse({"status": "error",
                                 "message": "Оплата не захвачена",
                                 "details": response.text})

    def refund(self, payment, amount=None):
        """
        Возвращает средства.
        """
        refund_url = "https://api.cloudpayments.ru/payments/refund"
        params = {
            "TransactionId": payment.transaction_id,
            "Amount": amount if amount else payment.amount
        }
        response = requests.post(refund_url, data=params)
        if response.status_code == 200:
            payment.status = "refunded"
            payment.save()
            return JsonResponse({"status": "success",
                                 "message": "Платеж успешно возвращен"})
        else:
            return JsonResponse({"status": "error",
                                 "message": "Ошибка при возврате платежа",
                                 "details": response.text})
