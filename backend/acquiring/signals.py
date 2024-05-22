from django.dispatch import receiver
from django.db.models.signals import post_save

from .utils import send_payment_email
from ..cloudpayments.models import CloudPayment
from ..mixplat.models import MixPlat


@receiver(post_save, sender=CloudPayment)
@receiver(post_save, sender=MixPlat)
def payment_handler(sender, instance, created, **kwargs):
    if not created:
        if instance.status == "rejected":
            user_email = instance.email
            message = f"Ваш платеж на {instance.amount} был отклонен."
            send_payment_email(user_email, message)
        else:
            user_email = instance.email
            message = f"Ваш платеж на {instance.amount} был обновлен."
            send_payment_email(user_email, message)
    else:
        user_email = instance.email
        message = f"Ваш платеж на {instance.amount} выполнен."
        send_payment_email(user_email, message)
