from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.permissions import IsAdminUser

from rootapp.models import Resident, Issue
from residentapp.api.serializers import IssueSerializer


class ListIssues(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        queryset = Issue.objects.all()
        serializer = IssueSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ListResidents(APIView):
    def get(self, request: Request):
        queryset = Resident.objects.all()
        return Response({"detail": "unimplemented"}, status=status.HTTP_204_NO_CONTENT)
