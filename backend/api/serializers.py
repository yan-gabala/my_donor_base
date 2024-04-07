# Модуль сериализаторов API.
from rest_framework import serializers

from donations.models import Donation


class DonationSerializer(serializers.ModelSerializer):
    """Сериализатор пожертвований."""

    class Meta:
        model = Donation
        fields = (
            "id",
            "email",
            "donat",
            "custom_donat",
            "payment_method",
            "monthly_donat",
            "subscription",
        )
