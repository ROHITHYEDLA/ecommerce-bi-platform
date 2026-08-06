from rest_framework import serializers

from .models import PurchaseOrder
from .models import PurchaseOrderItem


class PurchaseOrderItemSerializer(serializers.ModelSerializer):

    total_cost = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
        read_only=True,
    )

    class Meta:
        model = PurchaseOrderItem
        fields = "__all__"


class PurchaseOrderSerializer(serializers.ModelSerializer):

    items = PurchaseOrderItemSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = PurchaseOrder
        fields = "__all__"