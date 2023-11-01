from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render
from django.views.generic import View
from residentapp.utils import is_resident


class ResidentViewProvider(LoginRequiredMixin, View):
    def get(self, request):
        if is_resident(request.user):
            return render(request, 'residentapp/resident-home.html')
        return render(request, 'rootapp/invalid-noaccess.html', {'message': "You are not an authorized resident."})
