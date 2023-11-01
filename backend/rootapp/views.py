from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from .api.endpoints import api_endpoints
from .models import Resident, Guard
from .utils import is_admin, view_for_this_request

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

frontend_urls = {
    'login-url': 'http://localhost:5173/',
    'admin-home': 'admin/',
}


class AuthCheckView(APIView):
    def get(self, request: Request):
        # print(request.headers)
        print(f"User: {request.user}")
        # print(f"Auth: {request.auth}")
        return Response({}, status=status.HTTP_307_TEMPORARY_REDIRECT)

    def post(self, request):
        data = request.data
        print(type(data))
        return Response({'message': 'Ok.'}, status=status.HTTP_200_OK)


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        return view_for_this_request(request)


class LogIn(View):
    def get(self, request):
        return render(request, 'rootapp/login.html')

    def post(self, request):
        username = request.POST["username"]
        human_id = request.POST['human-id']
        password = request.POST["passo"]

        user = authenticate(username=username, password=password)

        if user is not None:
            # if validated user is only admin
            # bug here
            if is_admin(user):
                login(request, user)
                return redirect(frontend_urls['admin-home'])

            human_id_prefix = human_id[0:2].upper() if len(human_id) >= 2 else ''

            # if validated user is a resident
            if human_id_prefix == 'RS':
                try:
                    assert Resident.objects.get(resident_id=human_id)
                    login(request, user)
                    return redirect('residentapp:resident-home')
                except Resident.DoesNotExist:
                    context = {'message': 'There are no resident registered within this human-id.'}
                    return render(request, 'rootapp/invalid-noaccess.html', context)

            # if validated user is a guard
            elif human_id_prefix == 'GA':
                try:
                    assert Guard.objects.get(guard_id=human_id)
                    login(request, user)
                    return redirect('guardapp:guard-home')
                except Guard.DoesNotExist:
                    context = {'message': 'There are no guard registered within this human-id.'}
                    return render(request, 'rootapp/invalid-noaccess.html', context)

        else:
            context = {'message': 'No user matches within this username and password.'}
            return render(request, 'rootapp/invalid-noaccess.html', context)

        # default Response
        return HttpResponse("No content - 204. Lack somewhere in backend.", status=status.HTTP_204_NO_CONTENT)


class LogOut(View):
    def get(self, request):
        logout(request)
        return render(request, 'rootapp/logout.html')


class EndPoints(LoginRequiredMixin, View):
    def get(self, request):
        if is_admin(request.user):
            context = {'urls': [reverse(f"root-app:{a.name}") for a in api_endpoints]}
            return render(request, 'rootapp/endpoints.html')

        context = {'message': 'This page has Admin access only.'}
        return render(request, 'rootapp/invalid-noaccess.html', context)
