from django.db import models
from django.conf import settings

from donor_base.base_model import BaseModelDonation


class CloudPayment(BaseModelDonation):
    """
    Модель платежа Cloudpayment.
    """

    payment_id = models.IntegerField(
        verbose_name="Индентификатор платежа",
    )
    status = models.CharField(
        max_length=settings.MAX_PAYMENT_STATUS_LENGTH,
        choices=settings.CLOUDPAYMENTS_CHOICES,
        verbose_name="Статус платежа",
    )
    user_account_id = models.IntegerField(
        verbose_name="Идентификатор пользователя",
    )
    date_created = models.DateField(
        auto_now_add=False,
        verbose_name="Дата создания платежа",
    )
    date_processed = models.DateField(
        auto_now_add=False,
        verbose_name="Дата обработки платежа",
    )
    payment_operator = models.CharField(
        max_length=settings.MAX_PAYMENT_OPERATOR_LENGTH,
        verbose_name="Платежный оператор",
    )
    currency = models.CharField(
        max_length=settings.MAX_CURRENCY_LENGTH,
        verbose_name="Валюта платежа",
    )

    class Meta:
        ordering = ("-pub_date", "payment_status")
        verbose_name = "Пожертвование Cloudpayment"
        verbose_name_plural = "Пожертвования Cloudpayment"
