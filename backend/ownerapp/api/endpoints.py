from django.urls import path
from .views import ListIssues

# owner/
#       residents/all/
#       resident/new/
#       resident/:resident_id/
#       resident/update/:resident_id/
#       resident/delete/:resident_id/

endpoints = [
    path('issues/all/', ListIssues.as_view(), name='list-issues'),
]
