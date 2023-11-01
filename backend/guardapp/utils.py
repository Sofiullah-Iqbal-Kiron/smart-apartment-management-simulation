from django.contrib.auth.models import User
from rootapp.models import Human, Guard


def is_guard(user: User):
    try:
        a_human: Human = user.the_human
        assert a_human.the_guard
        return True
    except Human.DoesNotExist:
        return False
    except Guard.DoesNotExist:
        return False
