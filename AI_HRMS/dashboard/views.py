import matplotlib.pyplot as plt
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
import matplotlib
matplotlib.use('Agg')
from employees.models import Employee
from departments.models import Department
from attendance.models import Attendance
from leaves.models import Leave
from payroll.models import Payroll

from accounts.decorators import (
    admin_required,
    hr_required,
    employee_required
)


@admin_required
def admin_dashboard(request):

    total_employees = Employee.objects.count()

    department_count = Department.objects.count()

    present_today = Attendance.objects.filter(
        date=timezone.now().date()
    ).count()

    pending_leaves = Leave.objects.filter(
        status="PENDING"
    ).count()

    payroll_records = Payroll.objects.count()

    context = {
        "total_employees": total_employees,
        "department_count": department_count,
        "present_today": present_today,
        "pending_leaves": pending_leaves,
        "payroll_records": payroll_records,
    }

    return render(
        request,
        "dashboard/admin_dashboard.html",
        context
    )


@hr_required
def hr_dashboard(request):

    return render(
        request,
        "dashboard/hr_dashboard.html"
    )


@employee_required
def employee_dashboard(request):

    employee = Employee.objects.get(
        user=request.user
    )

    attendance_count = Attendance.objects.filter(
        employee=employee
    ).count()

    leave_count = Leave.objects.filter(
        employee=employee
    ).count()

    payroll_count = Payroll.objects.filter(
        employee=employee
    ).count()

    context = {
        "employee": employee,
        "attendance_count": attendance_count,
        "leave_count": leave_count,
        "payroll_count": payroll_count,
    }

    return render(
        request,
        "dashboard/employee_dashboard.html",
        context
    )


def attendance_chart(request):

    labels = [
        "Present",
        "Absent"
    ]

    values = [
        80,
        20
    ]

    plt.figure(figsize=(5, 4))

    plt.bar(
        labels,
        values
    )

    plt.title(
        "Attendance Summary"
    )

    plt.savefig(
        "static/chart.png"
    )

    plt.close()

    return render(
        request,
        "dashboard/chart.html"
    )
