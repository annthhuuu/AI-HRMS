from django.db import models
from accounts.models import User
from departments.models import Department


class Employee(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True
    )

    phone = models.CharField(
        max_length=15
    )

    address = models.TextField()

    joining_date = models.DateField()

    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username}"
        