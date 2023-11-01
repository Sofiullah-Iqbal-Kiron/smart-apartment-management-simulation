from django.urls import path
from .views import ResidentViewProvider
from .api.endpoints import paths

from rest_framework.urlpatterns import format_suffix_patterns

app_name = "residentapp"

urlpatterns = [
                  path('home/', ResidentViewProvider.as_view(), name='resident-home')
              ] + paths

urlpatterns = format_suffix_patterns(urlpatterns)
