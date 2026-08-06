from django.db import transaction
from django.core.exceptions import ValidationError

from inventory.models import Inventory, InventoryTransaction


class StockService:

    @staticmethod
    @transaction.atomic
    def stock_in(
        inventory: Inventory,
        quantity: int,
        created_by=None,
        reference: str = "",
        remarks: str = "",
    ):
        if quantity <= 0:
            raise ValidationError("Quantity must be greater than zero.")

        inventory.current_stock += quantity
        inventory.save()

        InventoryTransaction.objects.create(
            inventory=inventory,
            transaction_type="STOCK_IN",
            quantity=quantity,
            reference=reference,
            remarks=remarks,
            created_by=created_by,
        )

        return inventory

    @staticmethod
    @transaction.atomic
    def stock_out(
        inventory: Inventory,
        quantity: int,
        created_by=None,
        reference: str = "",
        remarks: str = "",
    ):
        if quantity <= 0:
            raise ValidationError("Quantity must be greater than zero.")

        if inventory.current_stock < quantity:
            raise ValidationError("Insufficient stock.")

        inventory.current_stock -= quantity
        inventory.save()

        InventoryTransaction.objects.create(
            inventory=inventory,
            transaction_type="STOCK_OUT",
            quantity=quantity,
            reference=reference,
            remarks=remarks,
            created_by=created_by,
        )

        return inventory

    @staticmethod
    @transaction.atomic
    def return_stock(
        inventory: Inventory,
        quantity: int,
        created_by=None,
        reference: str = "",
        remarks: str = "",
    ):
        if quantity <= 0:
            raise ValidationError("Quantity must be greater than zero.")

        inventory.current_stock += quantity
        inventory.save()

        InventoryTransaction.objects.create(
            inventory=inventory,
            transaction_type="RETURN",
            quantity=quantity,
            reference=reference,
            remarks=remarks,
            created_by=created_by,
        )

        return inventory

    @staticmethod
    @transaction.atomic
    def damage_stock(
        inventory: Inventory,
        quantity: int,
        created_by=None,
        reference: str = "",
        remarks: str = "",
    ):
        if quantity <= 0:
            raise ValidationError("Quantity must be greater than zero.")

        if inventory.current_stock < quantity:
            raise ValidationError("Insufficient stock.")

        inventory.current_stock -= quantity
        inventory.save()

        InventoryTransaction.objects.create(
            inventory=inventory,
            transaction_type="DAMAGE",
            quantity=quantity,
            reference=reference,
            remarks=remarks,
            created_by=created_by,
        )

        return inventory

    @staticmethod
    @transaction.atomic
    def adjust_stock(
        inventory: Inventory,
        new_quantity: int,
        created_by=None,
        reference: str = "",
        remarks: str = "",
    ):
        if new_quantity < 0:
            raise ValidationError("Quantity cannot be negative.")

        difference = new_quantity - inventory.current_stock

        inventory.current_stock = new_quantity
        inventory.save()

        InventoryTransaction.objects.create(
            inventory=inventory,
            transaction_type="ADJUSTMENT",
            quantity=abs(difference),
            reference=reference,
            remarks=remarks,
            created_by=created_by,
        )

        return inventory

    @staticmethod
    def validate_stock(inventory: Inventory, quantity: int):
        return inventory.current_stock >= quantity