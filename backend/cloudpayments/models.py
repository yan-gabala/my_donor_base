from decimal import Decimal

from django.db import models

from payments import PurchasedItem
from donations.models import Donation


class CloudPayment(Donation):
    """
    Модель платежа Cloudpayment.
    """

    payment_status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Ожидание"),
            ("success", "Успешно"),
            ("failure", "Ошибка")
        ],
        default="pending",
        verbose_name="Статус платежа"
    )

    class Meta:
        ordering = ("-pub_date",)
        verbose_name = "Пожертвование Cloudpayment"
        verbose_name_plural = "Пожертвования Cloudpayment"

    def get_failure_url(self):
        """
        Возвращает URL, на который будет перенаправлен пользователь
        при неудачном платеже.
        """
        return f"http://example.com/payments/{self.pk}/failure"

    def get_success_url(self):
        """
        Возвращает URL, на который будет перенаправлен пользователь
        при успешнои платеже.
        """
        return f"http://example.com/payments/{self.pk}/success"

    def get_purchased_items(self):
        """
        Возвращает атрибуты платежа.
        """
        yield PurchasedItem(
            name="Платеж Cloudpayment",
            sku="СloudPayment",
            quantity=1,
            price=Decimal(self.donat or self.custom_donat),
            currency="RUB",
        )
