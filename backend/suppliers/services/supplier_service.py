from django.shortcuts import get_object_or_404

from suppliers.models import Supplier


class SupplierService:

    @staticmethod
    def create_supplier(**data):
        return Supplier.objects.create(**data)

    @staticmethod
    def list_suppliers():
        return Supplier.objects.all()

    @staticmethod
    def get_supplier(supplier_id):
        return get_object_or_404(
            Supplier,
            pk=supplier_id,
        )

    @staticmethod
    def update_supplier(supplier, **data):

        for field, value in data.items():
            setattr(supplier, field, value)

        supplier.save()

        return supplier

    @staticmethod
    def delete_supplier(supplier):
        supplier.delete()