import stripe
from django.db.models.signals import post_save
from django.dispatch import receiver

from ..cloudpayments.models import CloudPayment
from ..mixplat.models import MixPlat


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
            "payment_operator": payment_operator,  # Название платежного оператора (нужно добавить это поле в модели mixplat и cloudpayment) # noqa: E501
            "payment_method": instance.payment_method,
        },
    )
    if not payment_intent.created:
        print(f"Payment Intent wasn't created for {payment_operator}")
    else:
        print(f"Payment Intent created successfully for {payment_operator}")
