from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from employees.models import Employee
from attendance.models import Attendance
from leaves.models import Leave
from payroll.models import Payroll


@login_required
def chatbot_view(request):

    response_text = ""

    history = request.session.get(
        "chat_history",
        []
    )

    if request.method == "POST":

        question = request.POST.get(
            "question",
            ""
        ).lower()

        employee = Employee.objects.filter(
            user=request.user
        ).first()

        if question in ["hi", "hello", "hey"]:

            response_text = (
                f"Hello {request.user.username}! "
                f"How can I help you today?"
            )

        elif "name" in question:

            response_text = (
                f"Your name is {request.user.username}"
            )

        elif "email" in question:

            response_text = (
                f"Your email is {request.user.email}"
            )

        elif "department" in question and employee:

            response_text = (
                f"You belong to {employee.department}"
            )

        elif "attendance" in question and employee:

            attendance_count = Attendance.objects.filter(
                employee=employee
            ).count()

            response_text = (
                f"You have {attendance_count} attendance records."
            )

        elif "leave" in question and employee:

            leave_count = Leave.objects.filter(
                employee=employee
            ).count()

            response_text = (
                f"You have {leave_count} leave requests."
            )

        elif "salary" in question and employee:

            payroll = Payroll.objects.filter(
                employee=employee
            ).last()

            if payroll:

                response_text = (
                    f"Your latest salary is ₹{payroll.net_salary}"
                )

            else:

                response_text = (
                    "No payroll records found."
                )

        elif (
            "department" in question or
            "attendance" in question or
            "leave" in question or
            "salary" in question
        ):

            response_text = (
                "No employee profile was found for your account."
            )

        elif "help" in question:

            response_text = (
                "Ask about name, email, department, "
                "attendance, leave or salary."
            )

        else:

            response_text = (
                "Sorry, I don't understand that."
            )

        history.append(
            {
                "user": question,
                "bot": response_text
            }
        )

        request.session["chat_history"] = history

        if request.headers.get("x-requested-with") == "XMLHttpRequest":

            return JsonResponse(
                {
                    "user": question,
                    "bot": response_text
                }
            )

    return render(
        request,
        "chatbot/chat.html",
        {
            "history": history,
            "response": response_text
        }
    )

