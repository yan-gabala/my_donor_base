from django.dispatch import receiver
from django.db.models.signals import post_save

from .utils import send_payment_email
from cloudpayments.models import CloudPayment
from mixplat.models import MixPlat


@receiver(post_save, sender=CloudPayment)
@receiver(post_save, sender=MixPlat)
def payment_handler(sender, instance, created, **kwargs):
    email = instance.email
    if not created:
        if instance.status == "rejected":
            message = f"Ваш платеж на {instance.donat} был отклонен."
            send_payment_email(email, message)
        else:
            message = f"Ваш платеж на {instance.donat} был обновлен."
            send_payment_email(email, message)
    else:
        message = f"Ваш платеж на {instance.donat} выполнен."
        send_payment_email(email, message)
