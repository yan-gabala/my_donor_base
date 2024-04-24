from rest_framework import serializers

from .models import CloudPayment


class CloudpaymentsSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для модели CloudPayment.
    """

    class Meta:
        model = CloudPayment
        fields = "__all__"
