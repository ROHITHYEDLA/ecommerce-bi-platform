from rest_framework import serializers

from .models import Inventory, InventoryTransaction


class InventorySerializer(serializers.ModelSerializer):

    product_name = serializers.CharField(
        source="product.name",
        read_only=True,
    )

    available_stock = serializers.ReadOnlyField()

    class Meta:
        model = Inventory
        fields = [
            "id",
            "product",
            "product_name",
            "warehouse",
            "current_stock",
            "reserved_stock",
            "available_stock",
            "minimum_stock",
            "reorder_level",
            "maximum_stock",
            "last_updated",
        ]

        read_only_fields = [
            "current_stock",
            "reserved_stock",
            "available_stock",
            "last_updated",
        ]


class InventoryTransactionSerializer(serializers.ModelSerializer):

    product_name = serializers.CharField(
        source="inventory.product.name",
        read_only=True,
    )

    class Meta:
        model = InventoryTransaction
        fields = [
            "id",
            "inventory",
            "product_name",
            "transaction_type",
            "quantity",
            "reference",
            "remarks",
            "created_by",
            "created_at",
        ]

        read_only_fields = [
            "created_at",
        ]

class StockOperationSerializer(serializers.Serializer):
    """
    Serializer for all stock operations.
    """

    quantity = serializers.IntegerField(
        min_value=1,
    )

    reference = serializers.CharField(
        max_length=100,
        required=False,
        allow_blank=True,
    )

    remarks = serializers.CharField(
        required=False,
        allow_blank=True,
    )