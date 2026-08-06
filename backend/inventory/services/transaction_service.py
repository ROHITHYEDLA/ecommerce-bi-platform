from inventory.models import Inventory
from .stock_service import StockService


class TransactionService:

    @staticmethod
    def create_transaction(
        inventory,
        transaction_type,
        quantity,
        created_by=None,
        reference="",
        remarks="",
    ):

        if transaction_type == "STOCK_IN":
            return StockService.stock_in(
                inventory,
                quantity,
                created_by,
                reference,
                remarks,
            )

        elif transaction_type == "STOCK_OUT":
            return StockService.stock_out(
                inventory,
                quantity,
                created_by,
                reference,
                remarks,
            )

        elif transaction_type == "RETURN":
            return StockService.return_stock(
                inventory,
                quantity,
                created_by,
                reference,
                remarks,
            )

        elif transaction_type == "DAMAGE":
            return StockService.damage_stock(
                inventory,
                quantity,
                created_by,
                reference,
                remarks,
            )

        elif transaction_type == "ADJUSTMENT":
            return StockService.adjust_stock(
                inventory,
                quantity,
                created_by,
                reference,
                remarks,
            )

        raise ValueError("Invalid transaction type.")