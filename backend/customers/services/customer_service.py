from django.shortcuts import get_object_or_404

from customers.models import Customer


class CustomerService:

    @staticmethod
    def list_customers():
        return Customer.objects.select_related("user").all()

    @staticmethod
    def get_customer(customer_id):
        return get_object_or_404(Customer, pk=customer_id)

    @staticmethod
    def create_customer(**data):
        user = data.get("user")

        if user.role != "CUSTOMER":
            raise ValidationError(
                "Only users with the CUSTOMER role can have a customer profile."
            )
        if Customer.objects.filter(user=user).exists():
            raise ValidationError(
                "Customer profile already exists."
            )



        return Customer.objects.create(**data)

    
    @staticmethod
    def update_customer(customer, **data):
        for field, value in data.items():
            setattr(customer, field, value)
        customer.save()
        return customer

    @staticmethod
    def delete_customer(customer):
        customer.delete()