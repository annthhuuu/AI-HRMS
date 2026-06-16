from django.urls import path
from . import views

urlpatterns = [

    path(
        "admin-dashboard/",
        views.admin_dashboard,
        name="admin_dashboard"
    ),

    path(
        "hr-dashboard/",
        views.hr_dashboard,
        name="hr_dashboard"
    ),

    path(
        "employee-dashboard/",
        views.employee_dashboard,
        name="employee_dashboard"
    ),
]