from django.apps import AppConfig


class AcquiringConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "acquiring"

    # def ready(self):
    #     from . import signals
