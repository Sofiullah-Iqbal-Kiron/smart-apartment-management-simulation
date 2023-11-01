from django.urls import path
from .views import IndexView, LogIn, LogOut, EndPoints, AuthCheckView
from .api.endpoints import api_endpoints

from django.conf import settings
from django.conf.urls.static import static

app_name = 'rootapp'

urlpatterns = [
                  path('', IndexView.as_view(), name='index'),
                  path('login/', LogIn.as_view(), name='login'),
                  path('logout/', LogOut.as_view(), name='logout'),
                  path('endpoints/', EndPoints.as_view(), name='endpoints'),
              ] + api_endpoints

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
