from django.contrib import admin
from django.urls import path

from todo.views import IncomeExpensesViewSet, IncomeExpenseBalanceViewSet, ResultAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IncomeExpensesViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>/', IncomeExpensesViewSet.as_view({'get': 'retrieve', 'put': 'update', 'destroy': 'delete'})),
    path('balance/', IncomeExpenseBalanceViewSet.as_view({'get': 'list'})),
    path('balance/<int:pk>/', IncomeExpenseBalanceViewSet.as_view({'get': 'retrieve'})),
    path('result', ResultAPIView.as_view())
]
