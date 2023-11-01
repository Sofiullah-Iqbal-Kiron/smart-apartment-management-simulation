from django.core.exceptions import ValidationError


def guard_id_validator(given_id: str):
    if not given_id.startswith('GA-'):
        raise ValidationError("Guard id must start with 'GA-'")


def guard_gender_validator(gender: str):
    if gender.strip().lower() != 'male':
        raise ValidationError("Guard must be male. It's a deal bro.")
