from django.dispatch import receiver
from django.db.models.signals import post_save

from .utils import send_payment_email
from ..cloudpayments.models import CloudPayment
from ..mixplat.models import MixPlat
import stripe


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


@receiver(post_save, sender=CloudPayment)
@receiver(post_save, sender=MixPlat)
def record_payment(sender, instance, created, **kwargs):
    """Recording payments method"""

    payment_operator = instance.payment_operator
    payment_intent = stripe.PaymentIntent.create(
        amount=instance.amount,
        currency=instance.currency,
        metadata={
            "payment_id": instance.payment_id,
            "status": instance.status,
            "user_account_id": instance.user_account_id,
            "date_created": instance.date_created,
            "date_processed": instance.date_processed,
            "payment_operator": payment_operator,  # TODO: Название платежного оператора (нужно добавить это поле в модели mixplat и cloudpayment) # noqa: E501
            "payment_method": instance.payment_method,
        },
    )
    if not payment_intent.created:
        print(f"Payment Intent wasn't created for {payment_operator}")
    else:
        print(f"Payment Intent created successfully for {payment_operator}")
