from decimal import Decimal

from inventory.models import Inventory
from inventory.services import StockService

from .order_item_service import OrderItemService
from .order_service import OrderService


class CheckoutService:

    @staticmethod
    def checkout(
        customer,
        items,
        created_by=None,
    ):

        order = OrderService.create_order(
            customer=customer,
            order_number="TEMP",
            subtotal=Decimal("0.00"),
            tax=Decimal("0.00"),
            shipping_charge=Decimal("0.00"),
            discount=Decimal("0.00"),
            total_amount=Decimal("0.00"),
        )

        for item in items:

            inventory = Inventory.objects.get(
                product=item["product"]
            )

            StockService.stock_out(
                inventory,
                item["quantity"],
                created_by=created_by,
                reference=order.order_number,
                remarks="Customer Order",
            )

            OrderItemService.create_item(
                order=order,
                product=item["product"],
                quantity=item["quantity"],
                unit_price=item["product"].selling_price,
                total_price=(
                    item["product"].selling_price
                    * item["quantity"]
                ),
            )

        OrderItemService.calculate_total(order)

        return order