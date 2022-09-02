import datetime as dt

from django.core.exceptions import ValidationError


def validate_year(value):
    if not (value <= dt.date.today().year):
        raise ValidationError(
            'Год создания произведения не может быть в будущем!'
        )
    return value
