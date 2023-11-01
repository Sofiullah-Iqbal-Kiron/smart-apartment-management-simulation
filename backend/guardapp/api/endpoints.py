from django.urls import path

from .views import MyProfile, Profile, ListRecords, CreateRecord, RegisterGuest

# Prefix: guard/
#               profile/me/ :View profile of requested guard.
#               profile/<str:guard_id>/ :View profile of parameterized guard. [IsAuthenticated]

#               check/token/<str:token_key>/ :Check token validity.

#               records/all/ :List view all records created by this logged-in guard user.
#               record/create/ :Create a new record.
#               record/<int:record_id>/ :Retrieve record.
#               record/update/<int:record_id>/ :Update an existing record, no implementation now. Security issue.

#               register/guest/ :Register a guest.

endpoints = [
    path('profile/me/', MyProfile.as_view(), name='my-profile'),
    path('profile/<str:guard_id>/', Profile.as_view(), name='guard-profile'),

    path('records/all/', ListRecords.as_view(), name='list-records'),
    path('record/create/', CreateRecord.as_view(), name='create-record'),

    path('register-guest/', RegisterGuest.as_view(), name='register-guest'),
]
