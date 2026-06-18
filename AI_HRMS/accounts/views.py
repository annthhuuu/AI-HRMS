from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

from django.contrib.auth.hashers import make_password

from django.contrib import messages

from .models import User
from .forms import UserForm

from accounts.decorators import admin_required


def login_view(request):

    if request.method == "POST":

        username = request.POST.get(
            "username"
        )

        password = request.POST.get(
            "password"
        )

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(
                request,
                user
            )

            if user.role == "ADMIN":

                return redirect(
                    "admin_dashboard"
                )

            elif user.role == "HR":

                return redirect(
                    "hr_dashboard"
                )

            else:

                return redirect(
                    "employee_dashboard"
                )

        else:

            messages.error(
                request,
                "Invalid Username or Password"
            )

    return render(
        request,
        "accounts/login.html"
    )


def logout_view(request):

    logout(
        request
    )

    return redirect(
        "login"
    )


@admin_required
def user_list(request):

    search = request.GET.get(
        "search"
    )

    users = User.objects.all()

    if search:

        users = users.filter(
            username__icontains=search
        )

    return render(
        request,
        "accounts/user_list.html",
        {
            "users": users
        }
    )


@admin_required
def user_create(request):

    if request.method == "POST":

        form = UserForm(
            request.POST
        )

        if form.is_valid():

            user = form.save(
                commit=False
            )

            password = form.cleaned_data.get(
                "password"
            )

            if password:

                user.password = make_password(
                    password
                )

            user.save()

            return redirect(
                "user_list"
            )

    else:

        form = UserForm()

    return render(
        request,
        "accounts/user_form.html",
        {
            "form": form,
            "title": "Add User"
        }
    )


@admin_required
def user_edit(request, user_id):

    user = get_object_or_404(
        User,
        id=user_id
    )

    if request.method == "POST":

        form = UserForm(
            request.POST,
            instance=user
        )

        if form.is_valid():

            user = form.save(
                commit=False
            )

            password = form.cleaned_data.get(
                "password"
            )

            if password:

                user.password = make_password(
                    password
                )

            user.save()

            return redirect(
                "user_list"
            )

    else:

        form = UserForm(
            instance=user
        )

    return render(
        request,
        "accounts/user_form.html",
        {
            "form": form,
            "title": "Edit User"
        }
    )


@admin_required
def user_delete(request, user_id):

    user = get_object_or_404(
        User,
        id=user_id
    )

    if request.method == "POST":

        user.delete()

        return redirect(
            "user_list"
        )

    return render(
        request,
        "accounts/user_confirm_delete.html",
        {
            "user_obj": user
        }
    )

