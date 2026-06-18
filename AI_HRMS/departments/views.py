from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from accounts.decorators import admin_required

from .models import Department


@admin_required
def department_list(request):

    search = request.GET.get(
        "search"
    )

    departments = Department.objects.all()

    if search:

        departments = departments.filter(
            name__icontains=search
        )

    return render(
        request,
        "departments/department_list.html",
        {
            "departments": departments
        }
    )


@admin_required
def add_department(request):

    if request.method == "POST":

        Department.objects.create(
            name=request.POST.get(
                "name"
            ),
            description=request.POST.get(
                "description"
            )
        )

        return redirect(
            "department_list"
        )

    return render(
        request,
        "departments/add_department.html"
    )


@admin_required
def edit_department(
    request,
    department_id
):

    department = get_object_or_404(
        Department,
        id=department_id
    )

    if request.method == "POST":

        department.name = request.POST.get(
            "name"
        )

        department.description = request.POST.get(
            "description"
        )

        department.save()

        return redirect(
            "department_list"
        )

    return render(
        request,
        "departments/edit_department.html",
        {
            "department": department
        }
    )


@admin_required
def delete_department(
    request,
    department_id
):

    department = get_object_or_404(
        Department,
        id=department_id
    )

    department.delete()

    return redirect(
        "department_list"
    )
