# Модуль собственных валидаторов.
from django.core.exceptions import ValidationError
from django.conf import settings


def forbidden_words_validator(value):
    """Валидация на запрещенные слова."""

    for forbidden_word in settings.FORBIDDEN_WORDS:
        if forbidden_word in value.lower():
            raise ValidationError(
                "Содержит запрещенные слова."
            )
