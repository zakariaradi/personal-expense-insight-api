from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from expenses.models import Expense
from datetime import datetime


class ExpensePermissionTests(APITestCase):
    def test_unauthenticated_user_cannot_access_expenses(self):
        response = self.client.get("/api/expenses/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class ExpenseCRUDTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )
        self.client.force_authenticate(user=self.user)

    def test_create_expense(self):
        data = {
            "amount": 100,
            "description": "Groceries",
            "category": "Food"
        }

        response = self.client.post("/api/expenses/", data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Expense.objects.count(), 1)
        self.assertEqual(Expense.objects.first().user, self.user)


class UserIsolationTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user("user1", password="123")
        self.user2 = User.objects.create_user("user2", password="123")

        Expense.objects.create(
            user=self.user1,
            amount=50,
            description="Food",
            category="Food"
        )

        Expense.objects.create(
            user=self.user2,
            amount=200,
            description="Rent",
            category="Rent"
        )

    def test_user_sees_only_own_expenses(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get("/api/expenses/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["category"], "Food")


class MonthlyAnalyticsTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user("user", password="123")
        self.client.force_authenticate(user=self.user)

        Expense.objects.create(
            user=self.user,
            amount=100,
            description="Food",
            category="Food",
            created_at=datetime(2025, 1, 10)
        )

        Expense.objects.create(
            user=self.user,
            amount=200,
            description="Rent",
            category="Rent",
            created_at=datetime(2025, 1, 20)
        )

    def test_monthly_insights(self):
        response = self.client.get("/api/expenses/monthly-insights/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertEqual(len(response.data["data"]), 1)


class DateFilterTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user("user", password="123")
        self.client.force_authenticate(user=self.user)

        Expense.objects.create(
            user=self.user,
            amount=100,
            description="Old expense",
            category="Food",
            created_at=datetime(2024, 12, 1)
        )

        Expense.objects.create(
            user=self.user,
            amount=300,
            description="New expense",
            category="Food",
            created_at=datetime(2025, 1, 5)
        )

    def test_filter_by_start_date(self):
        response = self.client.get(
            "/api/expenses/monthly-insights/?start_date=2025-01-01"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["data"]), 1)


class CategoryAnalyticsTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user("user", password="123")
        self.client.force_authenticate(user=self.user)

        Expense.objects.create(
            user=self.user,
            amount=100,
            description="Food 1",
            category="Food"
        )

        Expense.objects.create(
            user=self.user,
            amount=200,
            description="Food 2",
            category="Food"
        )

    def test_category_insights(self):
        response = self.client.get("/api/expenses/category-insights/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["data"][0]["total_spent"], 300)
        self.assertEqual(response.data["data"][0]["expense_count"], 2)