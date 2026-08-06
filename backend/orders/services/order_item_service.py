from orders.models import OrderItem


class OrderItemService:

    @staticmethod
    def create_item(**data):
        return OrderItem.objects.create(**data)

    @staticmethod
    def calculate_total(order):

        subtotal = 0

        for item in order.items.all():
            subtotal += item.total_price

        order.subtotal = subtotal
        order.total_amount = (
            subtotal
            + order.tax
            + order.shipping_charge
            - order.discount
        )

        order.save()

        return order