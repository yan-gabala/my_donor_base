# Модуль представления пожертвований.
from rest_framework import viewsets

from .serializers import DonationSerializer
from donations.models import Donation


class DonationViewSet(viewsets.ModelViewSet):
    """Вьюсет пожертвований."""

    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
