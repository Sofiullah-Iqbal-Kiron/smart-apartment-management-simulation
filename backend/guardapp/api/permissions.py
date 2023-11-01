from rest_framework.permissions import BasePermission
from rest_framework.request import Request

from ..utils import is_guard


class IsGuard(BasePermission):
    """
    Checks weather the requested user is a Guard or not.
    """

    message = "You are not a registered guard."

    def has_permission(self, request: Request, view):
        return is_guard(request.user)
