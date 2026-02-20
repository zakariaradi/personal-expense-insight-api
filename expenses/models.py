from django.db import models
from django.contrib.auth.models import User


class Expense(models.Model):
    """
    Expense model represents a single financial transaction
    created by a user.
    """

    # Reference to the user who owns the expense
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="expenses"
    )

    # Expense amount
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    # Short description of the expense
    description = models.CharField(
        max_length=255
    )

    # Category of the expense (e.g., Food, Transport, Rent)
    category = models.CharField(
        max_length=100
    )

    # Timestamp when the expense is created
    # Used for monthly analytics and insights
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        """
        String representation of the expense object.
        """
        return f"{self.user.username} - {self.amount} ({self.category})"
