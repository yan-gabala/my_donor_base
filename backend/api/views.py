# Модуль представлений проекта.
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .mixins import ViewListCreateMixinsSet
from .permissions import IsAdmin
from .serializers import (
    DonationSerializer,
    ContactSerializer,
    ForbiddenwordSerializer,
    CloudpaymentsSerializer,
)
from contacts.models import Contact
from donations.models import Donation
from forbiddenwords.models import ForbiddenWord


class DonationViewSet(viewsets.ModelViewSet):
    """Вьюсет пожертвований."""

    queryset = Donation.objects.all()
    serializer_class = DonationSerializer


class ContactViewSet(viewsets.ModelViewSet):
    """Вьюсет контактов."""

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ForbiddenwordViewSet(ViewListCreateMixinsSet):
    """Вьюсет запрещенных слов."""

    queryset = ForbiddenWord.objects.all()
    serializer_class = ForbiddenwordSerializer
    permission_classes = [IsAdmin]
    pagination_class = None


class CloudPaymentsViewSet(viewsets.GenericViewSet):
    """
    Вьсюсет для Cloudpayment.
    """

    @action(detail=False, url_path="create_cloudpayment", methods=["post"])
    def create_cloudpayment(self, request):
        """
        Создание экзепмляра Cloudpayment.
        """
        # При успешном создании платежа через Stripe, возвращается объект PaymentIntent.
        # Оттолкнулся от его структуры.
        data = {
            "email": request.data.get("receipt_email"),
            "donat": request.data.get("amount"),
            "payment_method": request.data.get("payment_method"),
            "payment_status": request.data.get("status"),
            "currency": request.data.get("currency")
        }
        serializer = CloudpaymentsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
