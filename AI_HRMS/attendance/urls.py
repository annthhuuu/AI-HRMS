from django.urls import path

from .views import (
    attendance_list,
    mark_attendance,
    edit_attendance,
    delete_attendance
)

urlpatterns = [

    path(
        "attendance-management/",
        attendance_list,
        name="attendance_list"
    ),

    path(
        "attendance-management/add/",
        mark_attendance,
        name="mark_attendance"
    ),

    path(
        "attendance-management/edit/<int:attendance_id>/",
        edit_attendance,
        name="edit_attendance"
    ),

    path(
        "attendance-management/delete/<int:attendance_id>/",
        delete_attendance,
        name="delete_attendance"
    ),

]