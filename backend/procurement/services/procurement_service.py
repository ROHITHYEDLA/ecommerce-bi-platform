from django.db import transaction
from django.utils import timezone

from inventory.models import Inventory
from inventory.services.stock_service import StockService

from procurement.models import PurchaseOrder


class ProcurementService:

    @staticmethod
    @transaction.atomic
    def receive_purchase_order(
        purchase_order,
        received_by=None,
    ):

        if purchase_order.status == "RECEIVED":
            raise ValueError(
                "Purchase Order already received."
            )

        for item in purchase_order.items.all():

            inventory, _ = Inventory.objects.get_or_create(
                product=item.product,
                defaults={
                    "warehouse": "Main Warehouse",
                },
            )

            StockService.stock_in(
                inventory=inventory,
                quantity=item.quantity,
                created_by=received_by,
                reference=purchase_order.po_number,
                remarks="Purchase Order Received",
            )

        purchase_order.status = "RECEIVED"
        purchase_order.received_date = timezone.now().date()
        purchase_order.save()

        return purchase_order