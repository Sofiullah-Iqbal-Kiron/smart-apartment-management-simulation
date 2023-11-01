from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from rootapp.models import Resident


class ListResidents(APIView):
    def get(self, request: Request):
        queryset = Resident.objects.all()
        return Response({"detail": "unimplemented"}, status=status.HTTP_204_NO_CONTENT)
