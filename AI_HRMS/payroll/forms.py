from django import forms

from .models import Payroll
from employees.models import Employee


class PayrollForm(forms.ModelForm):

    class Meta:
        model = Payroll
        fields = [
            "employee",
            "month",
            "basic_salary",
            "bonus",
            "deductions",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["employee"].queryset = Employee.objects.all()
        self.fields["month"].widget.attrs.update({
            "placeholder": "e.g. January 2026"
        })
