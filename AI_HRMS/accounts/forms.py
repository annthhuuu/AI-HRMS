from django import forms
from .models import User


class UserForm(forms.ModelForm):

    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "role",
            "password"
        ]

