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


class MixplatViewSet(viewsets.GenericViewSet):
    """Вьюсет Mixplat."""

    @action(detail=False, url_path="payment_status", methods=("post",))
    def payment_status(self, request):
        """Метод получения данных от Mixplat."""
        try:
            Donation.objects.create(
                email=request.data["user_email"],
                donat=request.data["amount"],
                custom_donat=request.data["amount_user"],
                payment_method=request.data["payment_method"],
            ).save()
            return Response(dict(result="ok"), status=status.HTTP_200_OK)
        except KeyError:
            return Response(
                dict(result="error", error_description="Internal error"),
                status=status.HTTP_400_BAD_REQUEST,
            )
