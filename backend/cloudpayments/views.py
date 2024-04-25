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
        payment_status = request.data.get("payment_status")
        cloudpayments_instance = CloudPayment(
            payment_status=payment_status,
            email=request.user.email,
            donat=amount,
            currency="RUB",
            payment_method="Cloudpayments",
            monthly_donat=False,
            subscription="",
        )
        cloudpayments_instance.save()
        serializer = CloudpaymentsSerializer(cloudpayments_instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
