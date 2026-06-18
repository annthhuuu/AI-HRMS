from django.urls import path

from .views import (
    login_view,
    logout_view,
    user_list,
    user_create,
    user_edit,
    user_delete
)

urlpatterns = [

    path(
        "",
        login_view,
        name="login"
    ),

    path(
        "login/",
        login_view,
        name="login"
    ),

    path(
        "logout/",
        logout_view,
        name="logout"
    ),

    path(
        "users/",
        user_list,
        name="user_list"
    ),

    path(
        "users/add/",
        user_create,
        name="user_create"
    ),

    path(
        "users/edit/<int:user_id>/",
        user_edit,
        name="user_edit"
    ),

    path(
        "users/delete/<int:user_id>/",
        user_delete,
        name="user_delete"
    ),

]