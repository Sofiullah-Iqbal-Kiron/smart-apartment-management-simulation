from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def guest_id_validator(given_id: str):
    if not given_id.startswith('GS-'):
        raise ValidationError("Guest id must start with 'GS-'")


def token_validator(token: str):
    # should be a regex validator as like username validator in User class
    pass