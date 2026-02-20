from rest_framework import serializers
from .models import Expense
import datetime


class ExpenseSerializer(serializers.ModelSerializer):
    """
    Serializer for the Expense model.
    Handles validation and serialization of expense data.
    """

    class Meta:
        model = Expense
        fields = "__all__"
        # The user field should not be provided by the client
        # It is automatically set from the authenticated user
        read_only_fields = ["user"]

    def validate_amount(self, value):
        """
        Ensure that the expense amount is greater than zero.
        """
        if value <= 0:
            raise serializers.ValidationError(
                "Amount must be greater than zero."
            )
        return value

    def validate(self, data):
        """
        Perform object-level validation.
        Prevent expenses from having a future date.
        """
        if data.get("date") and data["date"] > datetime.date.today():
            raise serializers.ValidationError(
                "Expense date cannot be in the future."
            )
        return data
