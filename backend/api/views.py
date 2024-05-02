# Модуль представлений проекта.
from rest_framework import viewsets
from rest_framework.decorators import action

from .mixins import ViewListCreateMixinsSet
from .permissions import IsAdmin
from .serializers import (
    DonationSerializer,
    ContactSerializer,
    ForbiddenwordSerializer,
    MixPlatSerializer,
)
from .utils import mixplat_request_handler
from contacts.models import Contact
from donations.models import Donation
from forbiddenwords.models import ForbiddenWord
from mixplat.models import MixPlat


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


class MixplatViewSet(viewsets.ModelViewSet):
    """Вьюсет Mixplat."""

    queryset = MixPlat.objects.all()
    serializer_class = MixPlatSerializer

    @action(detail=False, url_path="payment_status", methods=("post",))
    def payment_status(self, request):
        """Метод получения данных от Mixplat."""
        return mixplat_request_handler(request)
