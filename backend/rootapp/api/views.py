# django
from django.utils import timezone
from django.contrib.auth.models import User

# rest framework
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

# knox
import knox.auth as kn

# local-rootapp
from rootapp.models import (Human,
                            Resident,
                            Guard,
                            Guest,
                            Record,
                            TempToken)
from rootapp.api.serializers import HumanSerializer, RecordSerializer
from rootapp.utils import is_admin

# local-residentapp
from residentapp.utils import is_resident

# local-guardapp
from guardapp.utils import is_guard


class ListHuman(APIView):
    """
    List all human available in this system.
    Guard and Resident are Subclass of Human Superclass.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = Human.objects.all()
        serializer = HumanSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CheckID(APIView):
    """
    Check that parameterized id in the url is a valid guard/resident/guest id or not.
    Returns boolean 'exists'.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request: Request, human_id: str):
        id_prefix: str = human_id[0:3].upper()
        if id_prefix == 'RS-':
            try:
                Resident.objects.get(resident_id__exact=human_id.upper())
                return Response({'exists': True}, status=status.HTTP_200_OK)
            except Resident.DoesNotExist:
                return Response({'exists': False}, status=status.HTTP_204_NO_CONTENT)
        elif id_prefix == 'GS-':
            try:
                Guest.objects.get(guest_id__exact=human_id.upper())
                return Response({'exists': True}, status=status.HTTP_200_OK)
            except Guest.DoesNotExist:
                return Response({'exists': False}, status=status.HTTP_204_NO_CONTENT)
        elif id_prefix == 'GA-':
            try:
                Guard.objects.get(guard_id__exact=human_id.upper())
                return Response({'exists': True}, status=status.HTTP_200_OK)
            except Guard.DoesNotExist:
                return Response({'exists': False}, status=status.HTTP_204_NO_CONTENT)
        return Response({'exists': None})


class CheckTokenValidity(APIView):
    """
    Check that the parameterized token is valid or not.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request: Request, token_key: str) -> Response:
        valid: bool
        detail: str
        status_code: status

        try:
            the_token: TempToken = TempToken.objects.get(key=token_key)
            if timezone.now()<the_token.valid_till:
                valid = False
                detail = 'Token expired.'
                status_code = status.HTTP_204_NO_CONTENT
            else:
                valid = True
                detail = 'Valid token.'
                status_code = status.HTTP_200_OK
        except TempToken.DoesNotExist:
            valid = False
            detail = 'Token does not exists.'
            status_code = status.HTTP_204_NO_CONTENT

        return Response({'valid' : valid, 'detail' : detail}, status=status_code)


class Records(APIView):
    """
    List all records.
    Admin user get all records available in the system.
    Resident user list-view only his/her records.
    Guard user list-view records created by him.
    Just login as a user and hit the endpoint via GET request.
    """

    authentication_classes = [BasicAuthentication, SessionAuthentication, kn.TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        List records.
        """

        user: User = request.user
        queryset = None
        if is_resident(user):
            resident: Resident = Resident.objects.get(human__user=user)
            queryset = Record.objects.filter(who=resident)
        elif is_guard(user):
            guard: Guard = Guard.objects.get(human__user=user)
            queryset = Record.objects.filter(recorder=guard)
        elif is_admin(user):
            queryset = Record.objects.all()
        serializer = RecordSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
