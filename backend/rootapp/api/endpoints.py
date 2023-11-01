from django.urls import path

from .views import ListHuman, CheckID, CheckTokenValidity, Records

api_endpoints = [
    path('human/list/', ListHuman.as_view(), name='list-human'),

    path('check-id/<str:human_id>/', CheckID.as_view(), name='check-human-id'),
    path('check-token/<str:token_key>/', CheckTokenValidity.as_view(), name='check-token'),

    # guard related, cause only guard externally creates record
    path('records/', Records.as_view(), name='records'),
]
