from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from rootapp.utils import is_guard


class GuardViewProvider(LoginRequiredMixin, View):
    def get(self, request):
        if is_guard(request.user):
            return render(request, 'guardapp/index.html')
        return render(request, 'rootapp/invalid-noaccess.html',
                      {'message': "You are not an authorized guard."})
