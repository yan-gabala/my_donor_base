from donor_base.base_model import BaseModelDonation


class CloudPayment(BaseModelDonation):
    """
    Модель платежа Cloudpayment.
    """

    class Meta:
        ordering = ("-pub_date", "payment_status")
        verbose_name = "Пожертвование Cloudpayment"
        verbose_name_plural = "Пожертвования Cloudpayment"
