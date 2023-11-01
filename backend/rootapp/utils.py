from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import Human, TempToken

from guardapp.utils import is_guard
from residentapp.utils import is_resident


def is_admin(user: User):
    return user.is_staff and user.is_superuser and user.is_active


def view_for_this_request(request: HttpRequest) -> HttpResponse:
    """
    Return appropriate HttpResponse for this request.
    """
    user: User = request.user
    if is_admin(user):
        return redirect('admin/')
    if is_guard(user):
        return redirect('guardapp:guard-home')
    elif is_resident(user):
        return redirect('residentapp:resident-home')
    else:
        return render(request, 'rootapp/invalid-noaccess.html', {"message": "Unauthorized user."})


def get_guest_id(token: str):
    if len(token) != 12:
        raise AttributeError('Invalid token, length must be 12.')
    return f'GS-{token[-1:4:-1][::-1]}'


def is_unique_token(token: str):
    if len(token) != 12:
        raise AttributeError('Length of token must be 12.')
    tokens = TempToken.objects.all(token=token)
    if len(tokens) > 0:
        return False
    return True


def verify_token(token: str):
    if len(token) != 12:
        raise AttributeError('Length must be 12.')
    the_token = TempToken.objects.get(token=token)
    if the_token is None:
        raise LookupError('No such token delivered to any resident.')
