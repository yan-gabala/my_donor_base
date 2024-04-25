from django.db import models

from donations.models import Donation


class CloudPayment(Donation):
    """
    Модель платежа Cloudpayment.
    """

    payment_status = models.CharField(
        max_length=20,
        choices=[
            ("success", "Успешно"),
            ("failure", "Ошибка")
        ],
        verbose_name="Статус платежа"
    )

    class Meta:
        ordering = ("-pub_date", "payment_status")
        verbose_name = "Пожертвование Cloudpayment"
        verbose_name_plural = "Пожертвования Cloudpayment"
