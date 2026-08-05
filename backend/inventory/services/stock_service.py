from django.db import transaction

from inventory.models import Inventory, InventoryTransaction


class StockService:

    @staticmethod
    @transaction.atomic
    def add_stock(
        inventory,
        quantity,
        user=None,
        reference=None,
        remarks=None,
    ):
        """
        Add stock to inventory.
        """

        if quantity <= 0:
            return {
                "success": False,
                "message": "Quantity must be greater than zero."
            }

        inventory.current_stock += quantity
        inventory.save()

        InventoryTransaction.objects.create(
            inventory=inventory,
            transaction_type="STOCK_IN",
            quantity=quantity,
            reference=reference,
            remarks=remarks,
            created_by=user,
        )

        return {
            "success": True,
            "message": "Stock added successfully.",
            "data": inventory,
        }

    @staticmethod
    @transaction.atomic
    def remove_stock(
        inventory,
        quantity,
        user=None,
        reference=None,
        remarks=None,
    ):
        """
        Remove stock from inventory.
        """

        if quantity <= 0:
            return {
                "success": False,
                "message": "Quantity must be greater than zero."
            }

        if inventory.available_stock < quantity:
            return {
                "success": False,
                "message": "Insufficient available stock."
            }

        inventory.current_stock -= quantity
        inventory.save()

        InventoryTransaction.objects.create(
            inventory=inventory,
            transaction_type="STOCK_OUT",
            quantity=quantity,
            reference=reference,
            remarks=remarks,
            created_by=user,
        )

        return {
            "success": True,
            "message": "Stock removed successfully.",
            "data": inventory,
        }

    @staticmethod
    @transaction.atomic
    def reserve_stock(inventory, quantity):
        """
        Reserve stock for an order.
        """

        if quantity <= 0:
            return {
                "success": False,
                "message": "Quantity must be greater than zero."
            }

        if inventory.available_stock < quantity:
            return {
                "success": False,
                "message": "Not enough stock available."
            }

        inventory.reserved_stock += quantity
        inventory.save()

        return {
            "success": True,
            "message": "Stock reserved successfully.",
            "data": inventory,
        }

    @staticmethod
    @transaction.atomic
    def release_reserved_stock(inventory, quantity):
        """
        Release reserved stock.
        """

        if quantity <= 0:
            return {
                "success": False,
                "message": "Quantity must be greater than zero."
            }

        if inventory.reserved_stock < quantity:
            return {
                "success": False,
                "message": "Reserved stock is insufficient."
            }

        inventory.reserved_stock -= quantity
        inventory.save()

        return {
            "success": True,
            "message": "Reserved stock released successfully.",
            "data": inventory,
        }

    @staticmethod
    def has_sufficient_stock(inventory, quantity):
        """
        Check whether enough stock is available.
        """

        return inventory.available_stock >= quantity

    @staticmethod
    def is_low_stock(inventory):
        """
        Check whether inventory is below minimum stock.
        """

        return inventory.current_stock <= inventory.minimum_stock

    @staticmethod
    def needs_reorder(inventory):
        """
        Check whether inventory has reached reorder level.
        """

        return inventory.current_stock <= inventory.reorder_level