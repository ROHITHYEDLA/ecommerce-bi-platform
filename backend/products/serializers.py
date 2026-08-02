from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "slug",
            "category",
            "description",
            "brand",
            "sku",
            "barcode",
            "cost_price",
            "selling_price",
            "stock_quantity",
            "minimum_stock",
            "weight",
            "image",
            "is_active",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "slug",
            "created_at",
            "updated_at",
        ]