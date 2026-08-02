from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "category",
        "brand",
        "selling_price",
        "stock_quantity",
        "is_active",
    )

    search_fields = (
        "name",
        "sku",
        "brand",
    )

    list_filter = (
        "category",
        "brand",
        "is_active",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }