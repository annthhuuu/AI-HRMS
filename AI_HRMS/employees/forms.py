from django import forms

from accounts.models import User
from departments.models import Department

from .models import Employee


class EmployeeForm(forms.Form):

    username = forms.CharField(
        max_length=150
    )

    email = forms.EmailField()

    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(
            render_value=True
        )
    )

    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        required=False
    )

    phone = forms.CharField(
        max_length=15
    )

    address = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 3
            }
        )
    )

    joining_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "type": "date"
            }
        )
    )

    salary = forms.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __init__(self, *args, employee=None, **kwargs):

        super().__init__(*args, **kwargs)

        self.employee = employee

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

        self.fields["department"].widget.attrs["class"] = "form-select"

        if employee:
            self.fields["password"].help_text = (
                "Leave blank to keep the current password."
            )
        else:
            self.fields["password"].required = True

    def clean_username(self):

        username = self.cleaned_data["username"]

        users = User.objects.filter(
            username=username
        )

        if self.employee:
            users = users.exclude(
                id=self.employee.user_id
            )

        if users.exists():
            raise forms.ValidationError(
                "This username is already taken."
            )

        return username

    def save(self):

        if self.employee:
            employee = self.employee
            user = employee.user
        else:
            user = User(
                role="EMPLOYEE"
            )
            employee = Employee(
                user=user
            )

        user.username = self.cleaned_data["username"]
        user.email = self.cleaned_data["email"]

        password = self.cleaned_data.get(
            "password"
        )

        if password:
            user.set_password(
                password
            )

        user.save()

        employee.department = self.cleaned_data["department"]
        employee.phone = self.cleaned_data["phone"]
        employee.address = self.cleaned_data["address"]
        employee.joining_date = self.cleaned_data["joining_date"]
        employee.salary = self.cleaned_data["salary"]
        employee.save()

        return employee
