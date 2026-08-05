from django.contrib import admin
from .models import Inventory, InventoryTransaction


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product",
        "current_stock",
        "reserved_stock",
        "minimum_stock",
        "reorder_level",
        "maximum_stock",
        "available_stock",
        "last_updated",
    )

    search_fields = (
        "product__name",
        "product__sku",
    )

    list_filter = (
        "last_updated",
    )


@admin.register(InventoryTransaction)
class InventoryTransactionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "inventory",
        "transaction_type",
        "quantity",
        "reference",
        "created_by",
        "created_at",
    )

    search_fields = (
        "inventory__product__name",
        "reference",
    )

    list_filter = (
        "transaction_type",
        "created_at",
    )