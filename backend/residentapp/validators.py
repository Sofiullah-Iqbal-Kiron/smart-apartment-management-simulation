from django.core.exceptions import ValidationError


def resident_id_validator(given_id: str):
    if not given_id.startswith('RS-'):
        raise ValidationError("Resident id must start with 'RS-'")
