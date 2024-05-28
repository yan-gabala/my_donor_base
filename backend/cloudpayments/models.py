from django.db import models
from django.conf import settings

from donor_base.base_model import BaseModelDonation


class CloudPayment(BaseModelDonation):
    """
    Модель платежа Cloudpayment.
    """

    payment_status = models.CharField(
        max_length=settings.MAX_PAYMENT_STATUS_LENGTH,
        choices=settings.CLOUDPAYMENTS_CHOICES,
        verbose_name="Статус платежа",
    )
    currency = models.CharField(
        max_length=settings.MAX_CURRENCY_LENGTH, verbose_name="Валюта платежа"
    )

    class Meta:
        ordering = ("-pub_date", "payment_status")
        verbose_name = "Пожертвование Cloudpayment"
        verbose_name_plural = "Пожертвования Cloudpayment"
