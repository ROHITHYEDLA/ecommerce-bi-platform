import re
from rest_framework import serializers


def validate_phone(phone):
    """
    Validate Indian phone number.
    """

    pattern = r"^[6-9]\d{9}$"

    if not re.match(pattern, phone):
        raise serializers.ValidationError(
            "Enter a valid 10-digit Indian phone number."
        )

    return phone


def validate_password(password):
    """
    Password Policy
    """

    if len(password) < 8:
        raise serializers.ValidationError(
            "Password must contain at least 8 characters."
        )

    return password