from django.shortcuts import get_object_or_404

from customers.models import CustomerAddress


class AddressService:

    @staticmethod
    def list_addresses():
        return CustomerAddress.objects.select_related(
            "customer",
            "customer__user",
        ).all()

    @staticmethod
    def get_address(address_id):
        return get_object_or_404(
            CustomerAddress,
            pk=address_id,
        )

    @staticmethod
    def create_address(**data):
        return CustomerAddress.objects.create(**data)

    @staticmethod
    def update_address(address, **data):
        for field, value in data.items():
            setattr(address, field, value)
        address.save()
        return address

    @staticmethod
    def delete_address(address):
        address.delete()