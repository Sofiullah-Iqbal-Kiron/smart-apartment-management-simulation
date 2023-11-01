from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from .views import GuardViewProvider
from .api.endpoints import endpoints

app_name = 'guardapp'

# Prefix: guard/
urlpatterns = [
                  path('home/', GuardViewProvider.as_view(), name='guard-home')
              ] + endpoints
