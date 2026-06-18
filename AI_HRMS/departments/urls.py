from django.urls import path

from .views import (
    department_list,
    add_department,
    edit_department,
    delete_department
)

urlpatterns = [

    path(
        "departments/",
        department_list,
        name="department_list"
    ),

    path(
        "departments/add/",
        add_department,
        name="add_department"
    ),

    path(
        "departments/edit/<int:department_id>/",
        edit_department,
        name="edit_department"
    ),

    path(
        "departments/delete/<int:department_id>/",
        delete_department,
        name="delete_department"
    ),

]