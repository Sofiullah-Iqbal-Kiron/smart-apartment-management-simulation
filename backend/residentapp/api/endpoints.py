from django.urls import path

from .views import BasicAuth, CheckID, MyProfile, ResidentProfile, ListDeleteIssues, CreateIssue, RetrieveIssue, UpdateIssue, DeleteIssue, GetToken

# Prefix: resident/
#                  check/id/<str:resident_id>/ :Check that the resident exists who has resident_id as parameterized in the url.

#                  profile/me/ :View profile of requested, logged-in Resident.
#                  profile/<str:resident_id>/ :View profile of Resident who has id as parameterized.

#                  issues/all/ :List all issues of currently logged-in resident
#                  issue/<int:issue_id>/ :Retrieve an issue.
#                  issue/create/ :Create an issue.
#                  issue/update/<int:issue_id>/ :Update parameterized issue.
#                  issue/delete/<int:issue_id>/ :Delete parameterized issue.
#                  issues/delete/all/ :Delete all issues at once. Move to trash for 30 days.

#                  token/sought/ :Sought a token for his guests via post, provide nog, expiry

#                  bill/payment/<str:transaction_number>/ :Post transaction_number after paying a bill to owner's bank account. Then owner will confirm it. After that, popup signal will send to the resident.

paths = [
    path('auth/basic/', BasicAuth.as_view(), name='basic-auth'),
    path('check-id/<str:resident_id>/', CheckID.as_view(), name='check-resident-exists'),

    path('profile/me/', MyProfile.as_view(), name='my-profile'),
    path('profile/<str:resident_id>/', ResidentProfile.as_view(), name='resident-profile'),

    path('issues/all/', ListDeleteIssues.as_view(), name='list-all-issues'),
    path('issues/delete/all', ListDeleteIssues.as_view(), name='delete-all-issues'),
    path('issue/create/', CreateIssue.as_view(), name='create-issue'),
    path('issue/<int:issue_id>/', RetrieveIssue.as_view(), name='retrieve-issue'),
    path('issue/update/<int:issue_id>/', UpdateIssue.as_view(), name='update-issue'),
    path('issue/delete/<int:issue_id>/', DeleteIssue.as_view(), name='delete-issue'),

    path('token/sought/', GetToken.as_view(), name='provide-token'),
]
