from django.urls import path
from .views import my_payroll, salary_slip

urlpatterns = [

    path(
        "my-payroll/",
        my_payroll,
        name="my_payroll"
    ),

    path(
        "salary-slip/<int:payroll_id>/",
        salary_slip,
        name="salary_slip"
    ),
]