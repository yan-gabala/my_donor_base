# Generated by Django 4.2 on 2024-08-14 15:08

import api.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CloudPayment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=255,
                        validators=[api.validators.forbidden_words_validator],
                        verbose_name="Электронная почта",
                    ),
                ),
                (
                    "donat",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (0, "0"),
                            (300, "300"),
                            (500, "500"),
                            (1000, "1000"),
                            (3000, "3000"),
                        ],
                        default=0,
                        verbose_name="Размер пожертвования",
                    ),
                ),
                (
                    "custom_donat",
                    models.PositiveIntegerField(
                        default=0,
                        verbose_name="Кастомизированный размер пожертвования",
                    ),
                ),
                (
                    "payment_method",
                    models.CharField(
                        max_length=64, verbose_name="Способ оплаты"
                    ),
                ),
                (
                    "monthly_donat",
                    models.BooleanField(
                        default=False,
                        verbose_name="Чекбокс о ежемесячном пожертвовании",
                    ),
                ),
                (
                    "subscription",
                    models.BooleanField(
                        default=False,
                        verbose_name="Чекбокс об отмене подписки",
                    ),
                ),
                (
                    "pub_date",
                    models.DateTimeField(
                        auto_now_add=True,
                        verbose_name="Дата публикации пожертвования",
                    ),
                ),
                (
                    "payment_id",
                    models.CharField(
                        max_length=100, verbose_name="Идентификатор платежа"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        max_length=100, verbose_name="Статус платежа"
                    ),
                ),
                (
                    "user_account_id",
                    models.PositiveIntegerField(
                        verbose_name="Идентификатор пользователя"
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(verbose_name="Дата создания платежа"),
                ),
                (
                    "date_processed",
                    models.DateTimeField(
                        verbose_name="Дата обработки платежа"
                    ),
                ),
                (
                    "payment_operator",
                    models.CharField(
                        max_length=250, verbose_name="Платежный оператор"
                    ),
                ),
                (
                    "currency",
                    models.CharField(
                        max_length=10, verbose_name="Валюта платежа"
                    ),
                ),
            ],
            options={
                "verbose_name": "Пожертвование Cloudpayment",
                "verbose_name_plural": "Пожертвования Cloudpayment",
                "ordering": ("-pub_date", "status"),
            },
        ),
    ]
