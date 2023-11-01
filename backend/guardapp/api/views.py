from django.utils import timezone

# rest_framework
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# knox
import knox.auth as kn

# local
from rootapp.models import Human, Guard, Record, Resident, TempToken
from .serializers import GuardProfileSerializer, RecordSerializer
from .permissions import IsGuard


# Done.
class MyProfile(APIView):
    """
    Profile view of requested, logged-in Guard.
    """

    permission_classes = [IsAuthenticated, IsGuard]

    def get(self, request):
        guard: Guard = Guard.objects.get(human__user=request.user)
        serializer = GuardProfileSerializer(guard, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        """
        Edit your profile. Write another serializer to edit profile.
        """
        content = {
            'detail' : 'Edit your profile. But no implementation available now.'
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)


# Done.
class Profile(APIView):
    """
    Read GuardProfile if you are a valid system user: Admin, Guard, Resident.
    URL parameter: guard_id
    """

    permission_classes = [IsAuthenticated, (IsAdminUser | IsGuard)]

    def get(self, request, guard_id: str):
        guard_id = guard_id.upper().strip()
        if not guard_id[0:3].startswith('GA-'):
            return Response({'detail': "Not a valid guard id. Must start with - 'GA-'"})
        try:
            instance = Guard.objects.get(guard_id__exact=guard_id)
            serializer = GuardProfileSerializer(instance, context={'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Guard.DoesNotExist:
            return Response({'detail': 'No guard available within this id.'}, status=status.HTTP_204_NO_CONTENT)


class ListRecords(APIView):
    """
    List records created by logged-in Guard.
    """

    permission_classes = [IsAuthenticated, IsGuard]

    def get(self, request):
        guard: Guard = Guard.objects.get(human__user=request.user)
        queryset = Record.objects.filter(recorder=guard)
        serializer = RecordSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateRecord(APIView):
    """
    Create a new Record.
    """

    permission_classes = [IsAuthenticated, IsGuard]

    def post(self, request):
        data = request.data
        serializer = RecordSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        try:
            record_of = Resident.objects.get(resident_id__exact=serializer.validated_data['who'])
            serializer.validated_data['who'] = record_of
        except Resident.DoesNotExist:
            return Response({'detail': 'None of the Resident has this id, invalid resident_id.'}, status=status.HTTP_204_NO_CONTENT)
        try:
            current_human: Human = request.user.the_human
            current_guard: Guard = current_human.the_guard
            serializer.save(recorder=current_guard)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Human.DoesNotExist:
            return Response({'detail': 'You are neither a guard nor a resident.'}, status=status.HTTP_204_NO_CONTENT)
        except Guard.DoesNotExist:
            return Response({'detail': 'Only guard can create a single record at a time'}, status=status.HTTP_204_NO_CONTENT)


class RegisterGuest(APIView):
    """
    Register a guest.
    """

    def post(self, request: Request) -> Response:
        data = request.data
        content = {
            'detail': 'Incomplete implementation.'
        }
        return Response(content, status=status.HTTP_200_OK)
