from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum, Avg, Count
from django.db.models.functions import TruncMonth
from django.utils.dateparse import parse_date

from .models import Expense
from .serializers import ExpenseSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing expenses and providing analytics endpoints.
    """
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    # 🔒 Return only expenses of the authenticated user
    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    # 👤 Automatically associate expense with the logged-in user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # ==================================================
    # Monthly Insights
    # GET /api/expenses/monthly-insights/
    # Optional query params:
    # - start_date (YYYY-MM-DD)
    # - end_date (YYYY-MM-DD)
    # ==================================================
    @action(detail=False, methods=["get"], url_path="monthly-insights")
    def monthly_insights(self, request):
        expenses = self.get_queryset()

        start_date = request.query_params.get("start_date")
        end_date = request.query_params.get("end_date")

        # ✅ Validate dates
        if start_date and not parse_date(start_date):
            return Response(
                {"success": False, "error": "Invalid start_date format"},
                status=400
            )

        if end_date and not parse_date(end_date):
            return Response(
                {"success": False, "error": "Invalid end_date format"},
                status=400
            )

        # ✅ Apply date filtering
        if start_date:
            expenses = expenses.filter(created_at__gte=start_date)

        if end_date:
            expenses = expenses.filter(created_at__lte=end_date)

        # ✅ Monthly aggregation
        monthly_data = (
            expenses
            .annotate(month=TruncMonth("created_at"))
            .values("month")
            .annotate(
                total_spent=Sum("amount"),
                average_spent=Avg("amount"),
                expense_count=Count("id")
            )
            .order_by("month")
        )

        return Response({
            "success": True,
            "data": monthly_data
        })

    # ==================================================
    # Category-Based Analytics
    # GET /api/expenses/category-insights/
    # ==================================================
    @action(detail=False, methods=["get"], url_path="category-insights")
    def category_insights(self, request):
        expenses = self.get_queryset()

        category_data = (
            expenses
            .values("category")
            .annotate(
                total_spent=Sum("amount"),
                expense_count=Count("id")
            )
            .order_by("-total_spent")
        )

        return Response({
            "success": True,
            "data": category_data
        })

    # ==================================================
    # Overall Summary
    # GET /api/expenses/summary/
    # ==================================================
    @action(detail=False, methods=["get"], url_path="summary")
    def summary(self, request):
        expenses = self.get_queryset()

        data = expenses.aggregate(
            total_spent=Sum("amount"),
            average_spent=Avg("amount"),
            expense_count=Count("id")
        )

        return Response({
            "success": True,
            "data": {
                "total_spent": data["total_spent"] or 0,
                "average_spent": data["average_spent"] or 0,
                "expense_count": data["expense_count"]
            }
        })