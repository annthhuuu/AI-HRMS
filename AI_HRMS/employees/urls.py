from django.urls import path
from .views import (
    profile_view,
    my_attendance,
    my_leaves,
    my_payroll,
    employee_list,
    employee_create,
    employee_edit,
    employee_delete
)
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

    path(
        "my-leaves/",
        my_leaves,
        name="my_leaves"
    ),

    path(
        "employees/",
        employee_list,
        name="employee_list"
    ),

    path(
        "employees/add/",
        employee_create,
        name="employee_create"
    ),

    path(
        "employees/<int:employee_id>/edit/",
        employee_edit,
        name="employee_edit"
    ),

    path(
        "employees/<int:employee_id>/delete/",
        employee_delete,
        name="employee_delete"
    ),

    path(
        "my-payroll/",
        my_payroll,
        name="my_payroll"
    ),

]
