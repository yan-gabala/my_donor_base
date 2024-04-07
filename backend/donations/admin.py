# Модуль админки модели пожертвований.
from django.conf import settings
from django.contrib import admin

from .models import Donation


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    """Админ зона пожертвований."""

    list_display = (
        "email",
        "donat",
        "custom_donat",
        "payment_method",
        "monthly_donat",
        "subscription",
        "pub_date",
    )
    empty_value_display = settings.EMPTY_VALUE
    list_filter = ("pub_date",)
