from django.shortcuts import render
from django.http import HttpResponse

from reportlab.pdfgen import canvas

from .models import Payroll
from employees.models import Employee

from accounts.decorators import employee_required


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
        "payroll/my_payroll.html",
        {
            "payrolls": payrolls
        }
    )


@employee_required
def salary_slip(request, payroll_id):

    payroll = Payroll.objects.get(
        id=payroll_id
    )

    response = HttpResponse(
        content_type="application/pdf"
    )

    response[
        "Content-Disposition"
    ] = (
        f'attachment; '
        f'filename="salary_slip.pdf"'
    )

    p = canvas.Canvas(response)

    p.drawString(
        100,
        800,
        "AI HRMS Salary Slip"
    )

    p.drawString(
        100,
        760,
        f"Employee: {payroll.employee}"
    )

    p.drawString(
        100,
        730,
        f"Salary: ₹{payroll.net_salary}"
    )

    p.drawString(
        100,
        700,
        f"Month: {payroll.month}"
    )

    p.save()

    return response