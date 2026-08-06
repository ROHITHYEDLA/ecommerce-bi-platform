from rest_framework import serializers

from .models import Order, OrderItem


class OrderItemCreateSerializer(serializers.Serializer):

    product = serializers.IntegerField()

    quantity = serializers.IntegerField(
        min_value=1,
    )


class CheckoutSerializer(serializers.Serializer):

    customer = serializers.IntegerField()

    items = OrderItemCreateSerializer(
        many=True,
    )


class OrderItemSerializer(serializers.ModelSerializer):

    product_name = serializers.CharField(
        source="product.name",
        read_only=True,
    )

    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(
        many=True,
        read_only=True,
    )

    customer_email = serializers.CharField(
        source="customer.user.email",
        read_only=True,
    )

    class Meta:
        model = Order
        fields = "__all__"