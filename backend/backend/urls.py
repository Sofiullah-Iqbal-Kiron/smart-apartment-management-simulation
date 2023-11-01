from django.contrib import admin
from django.urls import include, path, re_path

from rest_framework.permissions import AllowAny

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from schema_graph.views import Schema

# api docs yasg
schema_view = get_schema_view(
    openapi.Info(
        title='Applications API',
        default_version='v1',
        description='Demo test description',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email='sofiul.k.1023@gmail.com'),
        license=openapi.License(name='BSD License'),
    ),
    public=True,
    permission_classes=[AllowAny]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schema/', Schema.as_view()),
    path('plate/', include('django_spaghetti.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path(r'api/knox/auth/', include('knox.urls')),

    # local apps
    path('', include('rootapp.urls')),
    path('resident/', include('residentapp.urls')),
    path('guard/', include('guardapp.urls')),
    path('owner/', include('ownerapp.urls')),

    # api docs with yasg
    # path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', 0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', 0)),
    path("__reload__/", include("django_browser_reload.urls")),
]
