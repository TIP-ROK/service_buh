from rest_framework import viewsets

from todo.models import IncomeExpense, IncomeExpenseBalance
from todo.serializers import IncomeExpensesSerializer, SumSerializer


class IncomeExpensesViewSet(viewsets.ModelViewSet):
    queryset = IncomeExpense.objects.all()
    serializer_class = IncomeExpensesSerializer


class IncomeExpenseBalanceViewSet(viewsets.ModelViewSet):
    queryset = IncomeExpenseBalance.objects.all()
    serializer_class = SumSerializer
