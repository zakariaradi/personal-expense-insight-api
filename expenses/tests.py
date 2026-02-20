from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Expense


class ExpenseAPITest(APITestCase):
    """
    Test suite for Expense API endpoints.
    """

    def setUp(self):
        """
        Create a test user and authenticate requests.
        """
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

        # Authenticate the test client
        self.client.force_authenticate(user=self.user)

    def test_create_expense(self):
        """
        Test creating a new expense.
        """
        url = reverse("expense-list")
        data = {
            "amount": 100,
            "description": "Groceries",
            "category": "Food"
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Expense.objects.count(), 1)
        self.assertEqual(Expense.objects.first().user, self.user)

    def test_expenses_are_user_specific(self):
        """
        Ensure that users can only access their own expenses.
        """
        Expense.objects.create(
            user=self.user,
            amount=50,
            description="Transport",
            category="Travel"
        )

        url = reverse("expense-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_monthly_insights_requires_authentication(self):
        """
        Ensure that the monthly insights endpoint requires authentication.
        """
        self.client.logout()
        url = reverse("expense-monthly-insights")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 401)

    def test_summary_endpoint_returns_correct_structure(self):
        """
        Test the summary endpoint response structure.
        """
        Expense.objects.create(
            user=self.user,
            amount=200,
            description="Food",
            category="Food"
        )

        url = reverse("expense-summary")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn("total_spent", response.data)
        self.assertIn("average_spent", response.data)
        self.assertIn("expense_count", response.data)
