from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from reportlab.pdfgen import canvas

from .models import Payroll
from .forms import PayrollForm
from employees.models import Employee

from accounts.decorators import admin_required, employee_required


@admin_required
def payroll_list(request):
    search = request.GET.get("search", "")

    payrolls = Payroll.objects.all().order_by("-generated_at")

    if search:
        payrolls = payrolls.filter(
            employee__user__username__icontains=search
        )

    return render(
        request,
        "payroll/payroll_list.html",
        {
            "payrolls": payrolls,
            "search": search,
        }
    )


@admin_required
def payroll_create(request):
    if request.method == "POST":
        form = PayrollForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("payroll_list")
    else:
        form = PayrollForm()

    return render(
        request,
        "payroll/payroll_form.html",
        {
            "form": form,
            "title": "Add Payroll",
        }
    )


@admin_required
def payroll_edit(request, payroll_id):
    payroll = get_object_or_404(
        Payroll,
        id=payroll_id
    )

    if request.method == "POST":
        form = PayrollForm(
            request.POST,
            instance=payroll
        )

        if form.is_valid():
            form.save()
            return redirect("payroll_list")
    else:
        form = PayrollForm(
            instance=payroll
        )

    return render(
        request,
        "payroll/payroll_form.html",
        {
            "form": form,
            "title": "Edit Payroll",
        }
    )


@admin_required
def payroll_delete(request, payroll_id):
    payroll = get_object_or_404(
        Payroll,
        id=payroll_id
    )

    if request.method == "POST":
        payroll.delete()
        return redirect("payroll_list")

    return render(
        request,
        "payroll/payroll_confirm_delete.html",
        {
            "payroll": payroll
        }
    )


@employee_required
def my_payroll(request):
    employee = get_object_or_404(
        Employee,
        user=request.user
    )

    payrolls = Payroll.objects.filter(
        employee=employee
    ).order_by("-generated_at")

    return render(
        request,
        "payroll/my_payroll.html",
        {
            "payrolls": payrolls
        }
    )


@employee_required
def salary_slip(request, payroll_id):
    payroll = get_object_or_404(
        Payroll,
        id=payroll_id
    )

    response = HttpResponse(
        content_type="application/pdf"
    )

    response[
        "Content-Disposition"
    ] = 'attachment; filename="salary_slip.pdf"'

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
        f"Month: {payroll.month}"
    )

    p.drawString(
        100,
        700,
        f"Basic Salary: Rs.{payroll.basic_salary}"
    )

    p.drawString(
        100,
        670,
        f"Bonus: Rs.{payroll.bonus}"
    )

    p.drawString(
        100,
        640,
        f"Deductions: Rs.{payroll.deductions}"
    )

    p.drawString(
        100,
        610,
        f"Net Salary: Rs.{payroll.net_salary}"
    )

    p.save()

    return response