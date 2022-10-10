from rest_framework import viewsets, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from todo.models import IncomeExpense, IncomeExpenseBalance
from todo.serializers import IncomeExpensesSerializer, SumSerializer


class IncomeExpensesViewSet(viewsets.ModelViewSet):
    queryset = IncomeExpense.objects.all()
    serializer_class = IncomeExpensesSerializer


class IncomeExpenseBalanceViewSet(viewsets.ModelViewSet):
    queryset = IncomeExpenseBalance.objects.all()
    serializer_class = SumSerializer


class ResultAPIView(views.APIView):
    # результат этойго класса сейчас не имеет возможности сохранять данные
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        sum_of_income = sum(IncomeExpense.objects.filter(is_expenses=True, user=request.user).values_list('amount', flat=True))
        sum_of_expense = sum(IncomeExpense.objects.filter(is_expenses=False, user=request.user).values_list('amount', flat=True))
        result = sum_of_income - sum_of_expense
        response_data = {
            'сумма расходов': sum_of_expense,
            'сумма доходов': sum_of_income,
            'результат': result

        }
        return Response(response_data, status=200)
