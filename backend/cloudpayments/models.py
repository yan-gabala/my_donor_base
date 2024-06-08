# Модуль модели платежей Cloudpayments
from django.conf import settings
from django.db import models

from donor_base.base_model import BaseModelDonation


class CloudPayment(BaseModelDonation):
    """
    Модель платежа Cloudpayment.
    """

    currency = models.CharField(
        max_length=settings.MAX_CURRENCY_LENGTH, verbose_name="Валюта платежа"
    )

    class Meta:
        ordering = ("-pub_date", "status")
        verbose_name = "Пожертвование Cloudpayment"
        verbose_name_plural = "Пожертвования Cloudpayment"
