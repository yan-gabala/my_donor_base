# Модуль представлений проекта.
from rest_framework import viewsets

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
