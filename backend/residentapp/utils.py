from django.contrib.auth.models import User
from django.utils import timezone
from rootapp.models import Human, Issue


def is_resident(user: User):
    try:
        a_human: Human = user.the_human
        assert a_human.the_resident
        return True
    except Exception:
        return False


def fill_length(word: str, length_be: int, fill_by: str):
    if len(fill_by) != 1:
        raise AttributeError('Length of fill_by must be 1.')
    return f'{fill_by}' * (length_be - len(word)) + word


def generate_a_temp_token():
    now = timezone.now()
    year = fill_length(str(now.year), 4, '0')
    month = fill_length(str(now.month), 2, '0')
    day = fill_length(str(now.day), 2, '0')
    hour = fill_length(str(now.hour), 2, '0')
    minute = fill_length(str(now.minute), 2, '0')
    second = fill_length(str(now.second), 2, '0')
    temp_token = hex(int(year + month + day + hour + minute + second))[2:].upper()

    return temp_token


def get_issue_instance(pk: int) -> Issue | None:
    try:
        instance = Issue.objects.get(pk=pk)
        return instance
    except Issue.DoesNotExist:
        return None