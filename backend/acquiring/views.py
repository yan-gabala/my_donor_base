import stripe
from django.db.models.signals import post_save
from django.dispatch import receiver

from ..cloudpayments.models import CloudPayment
from ..mixplat.models import MixPlat


# Сигнал post_save срабатывает только после успешного сохранения объекта модели
# (например, при создании нового объекта или обновлении существующего)
# при использовании метода create или save модели
# здесь речь не о пост-запросе, а о том, что сигнал сработает после сохранения объекта модели (post save) # noqa: E501
@receiver(post_save, sender=CloudPayment)
@receiver(post_save, sender=MixPlat)
def record_payment(sender, instance, created, **kwargs):
    # Получаем данные для создания платежного намерения
    amount = instance.amount
    payment_method = instance.payment_method
    payment_id = instance.payment_id
    status = instance.status
    user_account_id = instance.user_account_id
    date_created = instance.date_created
    date_processed = instance.date_processed
    currency = instance.currency
    # Название платежного оператора (нужно добавить это поле в модели mixplat и cloudpayment) # noqa: E501
    payment_operator = instance.operator

    payment_intent = stripe.PaymentIntent.create(
        amount=amount,
        payment_id=payment_id,
        status=status,
        user_account_id=user_account_id,
        date_created=date_created,
        date_processed=date_processed,
        currency=currency,
        metadata={
            "payment_operator": payment_operator,
            "payment_method": payment_method,
        },
    )
    if not payment_intent.created:
        print(f"Payment Intent wasn't created for {payment_operator}")
    else:
        print(f"Payment Intent created successfully for {payment_operator}")
