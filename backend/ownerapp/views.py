from django.views import View
from django.http import HttpResponse
from django.shortcuts import render


class IndexView(View):
    def get(self, request):
        return HttpResponse("Hello Owner.")
