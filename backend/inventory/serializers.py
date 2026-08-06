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
        fields = "__all__"


class InventoryTransactionSerializer(serializers.ModelSerializer):

    product_name = serializers.CharField(
        source="inventory.product.name",
        read_only=True,
    )

    class Meta:
        model = InventoryTransaction
        fields = "__all__"
        read_only_fields = (
            "created_by",
            "created_at",
        )