from .models import Product


class ProductService:

    @staticmethod
    def create_product(serializer):
        return serializer.save()

    @staticmethod
    def update_product(serializer):
        return serializer.save()

    @staticmethod
    def delete_product(product):
        product.delete()