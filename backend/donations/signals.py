# from django.dispatch import receiver
# from django.db.models.signals import post_save
#
# from .utils import send_payment_email
# from .models import Donation
#
#
# @receiver(post_save, sender=Donation)
# def payment_handler(sender, instance, created, **kwargs):
#     if not created and instance.status == "rejected":
# or another word status
#         user_email = instance.email
#         message = f"Ваш платеж на {instance.amount} был отклонен."
#         send_payment_email(user_email, message)
