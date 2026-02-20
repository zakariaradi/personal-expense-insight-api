from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum, Avg, Count
from django.db.models.functions import TruncMonth

from .models import Expense
from .serializers import ExpenseSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Return only expenses that belong to the authenticated user
    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    # Automatically associate the expense with the logged-in user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # ======================================
    # Monthly Insights Endpoint
    # GET /api/expenses/monthly-insights/
    # Returns:
    # - Total monthly spending
    # - Average spending
    # - Number of expenses per month
    # ======================================
    @action(detail=False, methods=["get"], url_path="monthly-insights")
    def monthly_insights(self, request):
        expenses = self.get_queryset()

        monthly_data = (
            expenses
            .annotate(month=TruncMonth("date"))
            .values("month")
            .annotate(
                total_spent=Sum("amount"),
                average_spent=Avg("amount"),
                expense_count=Count("id")
            )
            .order_by("month")
        )

        return Response(monthly_data)

    # ======================================
    # Overall Summary Endpoint
    # GET /api/expenses/summary/
    # Returns:
    # - Total spending
    # - Average spending
    # - Total number of expenses
    # ======================================
    @action(detail=False, methods=["get"], url_path="summary")
    def summary(self, request):
        expenses = self.get_queryset()

        data = expenses.aggregate(
            total_spent=Sum("amount"),
            average_spent=Avg("amount"),
            expense_count=Count("id")
        )

        return Response({
            "total_spent": data["total_spent"] or 0,
            "average_spent": data["average_spent"] or 0,
            "expense_count": data["expense_count"]
        })
