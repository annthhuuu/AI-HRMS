from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from accounts.decorators import admin_required

from employees.models import Employee
from attendance.models import Attendance


@admin_required
def attendance_list(request):

    search = request.GET.get("search")

    attendance_records = Attendance.objects.select_related(
        "employee"
    ).order_by("-date")

    if search:

        attendance_records = attendance_records.filter(
            employee__user__username__icontains=search
        )

    return render(
        request,
        "attendance/attendance_list.html",
        {
            "attendance_records": attendance_records
        }
    )


@admin_required
def mark_attendance(request):

    employees = Employee.objects.all()

    if request.method == "POST":

        employee = Employee.objects.get(
            id=request.POST.get("employee")
        )

        Attendance.objects.update_or_create(
            employee=employee,
            date=request.POST.get("date"),
            defaults={
                "status": request.POST.get("status")
            }
        )

        return redirect(
            "attendance_list"
        )

    return render(
        request,
        "attendance/attendance_form.html",
        {
            "employees": employees,
            "title": "Mark Attendance"
        }
    )


@admin_required
def edit_attendance(
    request,
    attendance_id
):

    attendance = get_object_or_404(
        Attendance,
        id=attendance_id
    )

    employees = Employee.objects.all()

    if request.method == "POST":

        attendance.employee = Employee.objects.get(
            id=request.POST.get("employee")
        )

        attendance.date = request.POST.get(
            "date"
        )

        attendance.status = request.POST.get(
            "status"
        )

        attendance.save()

        return redirect(
            "attendance_list"
        )

    return render(
        request,
        "attendance/attendance_form.html",
        {
            "attendance": attendance,
            "employees": employees,
            "title": "Edit Attendance"
        }
    )


@admin_required
def delete_attendance(
    request,
    attendance_id
):

    attendance = get_object_or_404(
        Attendance,
        id=attendance_id
    )

    if request.method == "POST":

        attendance.delete()

        return redirect(
            "attendance_list"
        )

    return render(
        request,
        "attendance/attendance_delete.html",
        {
            "attendance": attendance
        }
    )
