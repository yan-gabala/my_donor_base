# Модуль представления пожертвований.
from rest_framework import viewsets

from .serializers import DonationSerializer, ContactSerializer
from contacts.models import Contact
from donations.models import Donation


class DonationViewSet(viewsets.ModelViewSet):
    """Вьюсет пожертвований."""

    queryset = Donation.objects.all()
    serializer_class = DonationSerializer


class ContactViewSet(viewsets.ModelViewSet):
    """Вьюсет контактов."""

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
