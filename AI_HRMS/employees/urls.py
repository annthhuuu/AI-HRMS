from django.urls import path
from .views import profile_view, my_attendance

urlpatterns = [
    path(
        "profile/",
        profile_view,
        name="profile"
    ),
    path(
        "my-attendance/",
        my_attendance,
        name="my_attendance"
    ),
]