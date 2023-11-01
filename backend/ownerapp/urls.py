from django.urls import path

from .views import IndexView

app_name = 'ownerapp'
urlpatterns = [
    path('', IndexView.as_view(), name='owner-home'),
]
