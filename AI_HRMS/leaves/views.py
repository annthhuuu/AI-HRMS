from django.shortcuts import render, redirect, get_object_or_404

from .models import Leave
from accounts.decorators import admin_required
from django.core.mail import send_mail
from django.core.mail import send_mail
@admin_required
def leave_list(request):

    leaves = Leave.objects.all().order_by(
        "-applied_at"
    )

    return render(
        request,
        "leaves/leave_list.html",
        {
            "leaves": leaves
        }
    )


@admin_required
def approve_leave(request, leave_id):

    leave = Leave.objects.get(
        id=leave_id
    )

    leave.status = "APPROVED"
    leave.save()

    send_mail(
        subject="Leave Approved",
        message=(
            f"Hello,\n\n"
            f"Your leave request from "
            f"{leave.start_date} to "
            f"{leave.end_date} "
            f"has been approved."
        ),
        from_email=None,
        recipient_list=[
            leave.employee.user.email
        ],
    )

    return redirect(
        "leave_list"
    )

@admin_required
def reject_leave(request, leave_id):

    leave = Leave.objects.get(
        id=leave_id
    )

    leave.status = "REJECTED"
    leave.save()

    send_mail(
        subject="Leave Rejected",
        message=(
            f"Hello,\n\n"
            f"Your leave request from "
            f"{leave.start_date} to "
            f"{leave.end_date} "
            f"has been rejected."
        ),
        from_email=None,
        recipient_list=[
            leave.employee.user.email
        ],
    )

    return redirect(
        "leave_list"
    )