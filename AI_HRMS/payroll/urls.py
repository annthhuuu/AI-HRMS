from django.urls import path
from .views import (
    payroll_list,
    payroll_create,
    payroll_edit,
    payroll_delete,
    salary_slip,
)

urlpatterns = [

    path(
        "payroll/",
        payroll_list,
        name="payroll_list"
    ),

    path(
        "payroll/add/",
        payroll_create,
        name="payroll_create"
    ),

    path(
        "payroll/<int:payroll_id>/edit/",
        payroll_edit,
        name="payroll_edit"
    ),

    path(
        "payroll/<int:payroll_id>/delete/",
        payroll_delete,
        name="payroll_delete"
    ),

    path(
        "salary-slip/<int:payroll_id>/",
        salary_slip,
        name="salary_slip"
    ),
]