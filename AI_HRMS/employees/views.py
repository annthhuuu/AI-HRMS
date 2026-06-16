from django.shortcuts import render
from accounts.decorators import employee_required
from .models import Employee
from attendance.models import Attendance

@employee_required
def my_attendance(request):

    employee = Employee.objects.get(
        user=request.user
    )

    attendance = Attendance.objects.filter(
        employee=employee
    ).order_by('-date')

    return render(
        request,
        "employees/my_attendance.html",
        {
            "attendance": attendance
        }
    )

@employee_required
def profile_view(request):

    employee = Employee.objects.get(
        user=request.user
    )

    return render(
        request,
        "employees/profile.html",
        {
            "employee": employee
        }
    )
