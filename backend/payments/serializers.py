from rest_framework import serializers

from .models import Payment


class PaymentCreateSerializer(serializers.Serializer):

    order = serializers.IntegerField()

    payment_method = serializers.ChoiceField(
        choices=[
            "CASH",
            "CARD",
            "UPI",
            "BANK_TRANSFER",
        ]
    )

    remarks = serializers.CharField(
        required=False,
        allow_blank=True,
    )


class PaymentSerializer(serializers.ModelSerializer):

    customer = serializers.CharField(
        source="order.customer.user.email",
        read_only=True,
    )

    order_number = serializers.CharField(
        source="order.order_number",
        read_only=True,
    )

    class Meta:
        model = Payment
        fields = "__all__"