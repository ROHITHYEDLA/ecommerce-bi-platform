from .models import Product
from inventory.models import Inventory


class ProductService:

    @staticmethod
    def create_product(serializer):
        product = serializer.save()

        Inventory.objects.create(
            product=product,
            current_stock=0,
            reserved_stock=0,
            minimum_stock=5,
            reorder_level=10,
            maximum_stock=1000,
        )

        return product

    @staticmethod
    def update_product(serializer):
        return serializer.save()

    @staticmethod
    def delete_product(product):
        product.delete()