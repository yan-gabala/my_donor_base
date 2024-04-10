# Модуль админки модели контакты.
from django.conf import settings
from django.contrib import admin

from .models import Contact, ForbiddenWord


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Админ зона контактов."""

    list_display = (
        "username",
        "email",
        "subject",
        "comment"
    )
    empty_value_display = settings.EMPTY_VALUE
    list_filter = ("username",)


@admin.register(ForbiddenWord)
class ForbiddenWordAdmin(admin.ModelAdmin):
    """Админ зона для запрещенных слов."""

    list_display = (
        "forbidden_word"
    )
    empty_value_display = settings.EMPTY_VALUE
    list_filter = ("forbidden_word",)
