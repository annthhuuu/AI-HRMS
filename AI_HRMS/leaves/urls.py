from django.urls import path
from . import views

urlpatterns = [

    path(
        "leaves/",
        views.leave_list,
        name="leave_list"
    ),

    path(
        "leave/<int:leave_id>/approve/",
        views.approve_leave,
        name="approve_leave"
    ),

    path(
        "leave/<int:leave_id>/reject/",
        views.reject_leave,
        name="reject_leave"
    ),
]