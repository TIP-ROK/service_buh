from rest_framework import serializers

from todo.models import IncomeExpense, IncomeExpenseBalance


class IncomeExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeExpense
        fields = '__all__'

    def create(self, validated_data):
        obj = IncomeExpense.objects.create(**validated_data)
        if IncomeExpenseBalance.objects.filter(user=validated_data['user']).values_list('user_id', flat=True).first() != validated_data['user'].id:
            IncomeExpenseBalance.objects.create(
                user=validated_data['user']
            )

        return obj


class SumSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeExpenseBalance
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['sum_of_income'] = sum(IncomeExpense.objects.filter(is_expenses=True, user=instance.user).values_list('amount', flat=True))
        response['sum_of_expense'] = sum(IncomeExpense.objects.filter(is_expenses=False, user=instance.user).values_list('amount', flat=True))
        response['result'] = response['sum_of_income'] - response['sum_of_expense']

        return response
