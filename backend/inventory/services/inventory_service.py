from django.shortcuts import get_object_or_404

from inventory.models import Inventory
from products.models import Product


class InventoryService:

    @staticmethod
    def create_inventory(
        product,
        warehouse=None,
        current_stock=0,
        reserved_stock=0,
        minimum_stock=5,
        reorder_level=10,
        maximum_stock=1000,
    ):
        return Inventory.objects.create(
            product=product,
            warehouse=warehouse,
            current_stock=current_stock,
            reserved_stock=reserved_stock,
            minimum_stock=minimum_stock,
            reorder_level=reorder_level,
            maximum_stock=maximum_stock,
        )

    @staticmethod
    def get_inventory(inventory_id):
        return get_object_or_404(
            Inventory,
            pk=inventory_id,
        )

    @staticmethod
    def get_inventory_by_product(product_id):
        product = get_object_or_404(
            Product,
            pk=product_id,
        )

        return get_object_or_404(
            Inventory,
            product=product,
        )

    @staticmethod
    def list_inventory():
        return Inventory.objects.select_related(
            "product"
        ).all()

    @staticmethod
    def update_inventory(inventory, **kwargs):

        for field, value in kwargs.items():
            setattr(inventory, field, value)

        inventory.save()

        return inventory

    @staticmethod
    def delete_inventory(inventory):
        inventory.delete()