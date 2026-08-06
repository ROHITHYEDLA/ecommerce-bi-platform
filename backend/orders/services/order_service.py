from django.shortcuts import get_object_or_404

from orders.models import Order


class OrderService:

    @staticmethod
    def create_order(**data):
        return Order.objects.create(**data)

    @staticmethod
    def get_order(order_id):
        return get_object_or_404(
            Order,
            pk=order_id,
        )

    @staticmethod
    def list_orders():
        return Order.objects.select_related(
            "customer",
            "customer__user",
        ).prefetch_related(
            "items",
        )

    @staticmethod
    def update_order(order, **data):

        for field, value in data.items():
            setattr(order, field, value)

        order.save()

        return order

    @staticmethod
    def delete_order(order):
        order.delete()