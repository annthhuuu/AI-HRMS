from django.shortcuts import get_object_or_404, redirect, render

from accounts.decorators import employee_required
from accounts.decorators import admin_required

from .forms import EmployeeForm
from .models import Employee
from attendance.models import Attendance
from leaves.models import Leave
from payroll.models import Payroll

@admin_required
def employee_list(request):


    search = request.GET.get("search")

    employees = Employee.objects.all()

    if search:
        employees = employees.filter(
        user__username__icontains=search
    )

    return render(
    request,
    "employees/employee_list.html",
    {
        "employees": employees
    }
    )

@admin_required
def employee_create(request):

    if request.method == "POST":
        form = EmployeeForm(
            request.POST
        )

        if form.is_valid():
            form.save()

            return redirect(
                "employee_list"
            )

    else:
        form = EmployeeForm()

    return render(
        request,
        "employees/employee_form.html",
        {
            "form": form,
            "title": "Add Employee",
            "button_text": "Add Employee"
        }
    )


@admin_required
def employee_edit(request, employee_id):

    employee = get_object_or_404(
        Employee,
        id=employee_id
    )

    initial = {
        "username": employee.user.username,
        "email": employee.user.email,
        "department": employee.department,
        "phone": employee.phone,
        "address": employee.address,
        "joining_date": employee.joining_date.isoformat(),
        "salary": employee.salary
    }

    if request.method == "POST":
        form = EmployeeForm(
            request.POST,
            employee=employee
        )

        if form.is_valid():
            form.save()

            return redirect(
                "employee_list"
            )

    else:
        form = EmployeeForm(
            initial=initial,
            employee=employee
        )

    return render(
        request,
        "employees/employee_form.html",
        {
            "form": form,
            "title": "Edit Employee",
            "button_text": "Save Changes"
        }
    )


@admin_required
def employee_delete(request, employee_id):

    employee = get_object_or_404(
        Employee,
        id=employee_id
    )

    if request.method == "POST":
        user = employee.user
        user.delete()

        return redirect(
            "employee_list"
        )

    return render(
        request,
        "employees/employee_confirm_delete.html",
        {
            "employee": employee
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


@employee_required
def my_attendance(request):


    employee = Employee.objects.get(
    user=request.user
    )

    attendance = Attendance.objects.filter(
    employee=employee
    ).order_by("-date")

    return render(
    request,
    "employees/my_attendance.html",
    {
        "attendance": attendance
    }
    )


@employee_required
def my_leaves(request):


    employee = Employee.objects.get(
    user=request.user
    )

    if request.method == "POST":

        Leave.objects.create(
            employee=employee,
            start_date=request.POST.get(
                "start_date"
            ),
            end_date=request.POST.get(
                "end_date"
            ),
            reason=request.POST.get(
                "reason",
                ""
            )
        )

        return redirect(
            "my_leaves"
        )

    leaves = Leave.objects.filter(
    employee=employee
    ).order_by("-applied_at")

    waiting_leaves = leaves.filter(
        status="PENDING"
    )

    taken_leaves = leaves.filter(
        status="APPROVED"
    )

    return render(
    request,
    "employees/my_leaves.html",
    {
        "leaves": leaves,
        "waiting_leaves": waiting_leaves,
        "taken_leaves": taken_leaves
    }
    )


@employee_required
def my_payroll(request):

    employee = Employee.objects.get(
    user=request.user
    )

    payrolls = Payroll.objects.filter(
    employee=employee
    )

    return render(
    request,
    "employees/my_payroll.html",
    {
        "payrolls": payrolls
    }
    )

