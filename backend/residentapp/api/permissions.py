from rest_framework.request import Request
from rest_framework.permissions import BasePermission

from ..utils import is_resident


class IsResident(BasePermission):
    """
    Check weather the requested user is Resident or not.
    """
    message = "Resident access only."

    def has_permission(self, request: Request, view):
        return is_resident(request.user)
