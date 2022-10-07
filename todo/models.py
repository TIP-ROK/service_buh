from django.contrib.auth.models import User
from django.db import models


class IncomeExpense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_expenses = models.BooleanField(default=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    update = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name


class IncomeExpenseBalance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sum_of_income = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    sum_of_expense = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return f'{self.user.id}'
