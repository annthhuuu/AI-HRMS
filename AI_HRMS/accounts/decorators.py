from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def admin_required(view_func):

    @login_required
    def wrapper(request, *args, **kwargs):

        if request.user.role == "ADMIN":
            return view_func(request, *args, **kwargs)

        return redirect("login")

    return wrapper


def hr_required(view_func):

    @login_required
    def wrapper(request, *args, **kwargs):

        if request.user.role == "HR":
            return view_func(request, *args, **kwargs)

        return redirect("login")

    return wrapper


def employee_required(view_func):

    @login_required
    def wrapper(request, *args, **kwargs):

        if request.user.role == "EMPLOYEE":
            return view_func(request, *args, **kwargs)

        return redirect("login")

    return wrapper