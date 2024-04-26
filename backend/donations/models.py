# Модуль модели пожертвований.
from django.conf import settings
from django.db import models

from api.validators import forbidden_words_validator


class Donation(models.Model):
    """Модель пожертвований."""

    email = models.EmailField(
        max_length=settings.MAX_EMAIL_LENGTH,
        unique=True,
        validators=[forbidden_words_validator],
        verbose_name="Электронная почта",
    )
    donat = models.PositiveSmallIntegerField(
        choices=settings.AMOUNT,
        default=settings.ZERO,
        verbose_name="Размер пожертвования",
    )
    custom_donat = models.PositiveIntegerField(
        default=settings.ZERO,
        verbose_name="Кастомизированный размер пожертвования",
    )
    payment_method = models.CharField(
        max_length=settings.PAYMENT_METHOD_LENGTH,
        verbose_name="Способ оплаты",
    )
    monthly_donat = models.BooleanField(
        default=False,
        verbose_name="Чекбокс о ежемесячном пожертвовании",
    )
    subscription = models.BooleanField(
        default=False,
        verbose_name="Чекбокс об отмене подписки",
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата публикации пожертвования",
    )

    class Meta:
        ordering = ("-pub_date",)
        verbose_name = "Пожертвование"
        verbose_name_plural = "Пожертвования"
