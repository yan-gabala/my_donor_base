# Generated by Django 4.2 on 2024-08-15 19:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contacts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="donor",
            name="subcsription",
            field=models.BooleanField(
                default=False, verbose_name="Наличие подписки у донора"
            ),
        ),
    ]
