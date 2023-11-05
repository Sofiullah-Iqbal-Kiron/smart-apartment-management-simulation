from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.reverse import reverse
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from rootapp.models import Resident, Issue, TempToken

from ..utils import generate_a_temp_token, get_issue_instance
from .serializers import ResidentProfileSerializer, IssueSerializer, TempTokenSerializer
from .permissions import IsResident


class BasicAuth(APIView):
    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return Response({'is_authenticated':True}, status=status.HTTP_200_OK)
        return Response({'is_authenticated':False}, status=status.HTTP_204_NO_CONTENT)


class CheckID(APIView):
    """
    Check that any resident exists within this id or not.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, resident_id: str):
        try:
            Resident.objects.get(resident_id__exact=resident_id.strip())
            return Response({'resident_exists': True})
        except Resident.DoesNotExist:
            return Response({'resident_exists': False})


class MyProfile(APIView):
    """
    Profile view of requested, logged-in Resident User.
    """

    permission_classes = [IsAuthenticated, IsResident]

    def get(self, request):
        resident: Resident = Resident.objects.get(human__user=request.user)
        serializer = ResidentProfileSerializer(resident, context={"request":request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        """
        Edit my profile. Write another serializer to edit profile.
        """
        content = {
            'detail' : 'edit your profile, logged-in resident'
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)


class ResidentProfile(APIView):
    """
    Retrieve current authenticated Resident information.
    Useful for profile page.
    Read Only. Admin can create, update, delete a resident.
    Forbidden for Non-Resident user.
    """

    permission_classes = [IsAuthenticated, IsAdminUser | IsResident]

    def get(self, request, resident_id):
        try:
            resident = Resident.objects.get(resident_id=resident_id)
            serializer = ResidentProfileSerializer(resident)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Resident.DoesNotExist:
            return Response({'error': 'resident does not exists within this id'})


class ListDeleteIssues(APIView):
    """
    List-All/Delete-All Issues of logged-in Resident.
    """

    permission_classes = [IsAuthenticated, IsResident]

    def get_issues(self, request: Request):
        user: User = request.user
        resident: Resident = Resident.objects.get(human__user=user)
        return Issue.objects.filter(raised_by=resident)

    def get(self, request: Request):
        """
        List Issues of logged-in Resident.
        """

        serializer = IssueSerializer(self.get_issues(request), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request):
        """
        Delete all issues of logged-in Resident.
        """

        delete_count = self.get_issues(request).delete()
        return Response({'delete_count': delete_count}, status=status.HTTP_204_NO_CONTENT)


class CreateIssue(APIView):
    """
    Create a new issue of logged-in Resident.
    """

    permission_classes = [IsAuthenticated, IsResident]

    def post(self, request: Request):
        data = request.data
        serializer = IssueSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(raised_by=request.user.the_human.the_resident)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RetrieveIssue(APIView):
    """
    Retrieve an issue.
    """

    permission_classes = [IsAuthenticated, IsResident]

    def get(self, request, issue_id):
        instance = get_issue_instance(issue_id)
        if instance is None:
            return Response({'error': 'invalid issue-id, perhaps none of issues has this id'})
        if instance.raised_by is request.user.the_human.the_resident:
            return Response({'error': "that's not your issue"})
        serializer = IssueSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateIssue(APIView):
    """
    Update this issue.
    """

    permission_classes = [IsAuthenticated, IsResident]

    def put(self, request, issue_id):
        data = request.data
        instance = get_issue_instance(issue_id)
        serializer = IssueSerializer(instance=instance, data=data)
        serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response({'message': 'incomplete update method implementation'}, status=status.HTTP_204_NO_CONTENT)


class DeleteIssue(APIView):
    """
    Delete this issue.
    """

    permission_classes = [IsAuthenticated, IsResident]

    def delete(self, request, issue_id):
        instance = get_issue_instance(issue_id)
        if instance is None:
            return Response({'error': 'no deletion executed, maybe invalid issue_id'})
        if instance.raised_by != request.user.the_human.the_resident:
            return Response({'error': "that's not your issue, just leave"})
        instance.delete()
        return Response({'message': f'successfully deleted issue {issue_id}'}, status=status.HTTP_204_NO_CONTENT)


class GetToken(APIView):
    """
    Get a temporary token to be used in registration process of your guests.
    Provide "number_of_allowed_guests" : int
    """
    permission_classes = [IsAuthenticated, IsResident]

    def post(self, request):
        data = request.data
        serializer = TempTokenSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(fond_by=Resident.objects.get(human__user=request.user))
        return Response(serializer.data, status=status.HTTP_200_OK)
