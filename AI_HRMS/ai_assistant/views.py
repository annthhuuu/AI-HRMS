from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.crypto import get_random_string

from accounts.models import User
from employees.models import Employee
from departments.models import Department
from leaves.models import Leave


@login_required
def ai_data_entry(request):

    message = ""
    departments = Department.objects.all()

    if request.method == "POST":

        action = request.POST.get(
            "action"
        )

        if action == "apply_leave" and request.user.role == "EMPLOYEE":

            employee = Employee.objects.get(
                user=request.user
            )

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

            message = (
                "Leave request submitted for approval."
            )

        elif action == "add_employee" and request.user.role == "ADMIN":

            username = request.POST.get(
                "username"
            )

            if User.objects.filter(
                username=username
            ).exists():

                message = (
                    f"Username {username} already exists."
                )

            else:

                password = request.POST.get(
                    "password"
                ) or get_random_string(
                    10
                )

                user = User.objects.create_user(
                    username=username,
                    email=request.POST.get(
                        "email"
                    ),
                    password=password,
                    role="EMPLOYEE"
                )

                Employee.objects.create(
                    user=user,
                    department_id=request.POST.get(
                        "department"
                    ) or None,
                    phone=request.POST.get(
                        "phone",
                        ""
                    ),
                    address=request.POST.get(
                        "address",
                        ""
                    ),
                    joining_date=request.POST.get(
                        "joining_date"
                    ),
                    salary=request.POST.get(
                        "salary"
                    )
                )

                message = (
                    f"Employee {username} added successfully."
                )

    return render(
        request,
        "ai_assistant/data_entry.html",
        {
            "departments": departments,
            "message": message
        }
    )
