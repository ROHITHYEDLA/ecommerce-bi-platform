from inventory.models import InventoryTransaction


class TransactionService:

    @staticmethod
    def get_all_transactions():
        """
        Retrieve all inventory transactions.
        """

        transactions = (
            InventoryTransaction.objects
            .select_related(
                "inventory",
                "inventory__product",
                "created_by",
            )
            .all()
        )

        return {
            "success": True,
            "message": "Transactions retrieved successfully.",
            "data": transactions,
        }

    @staticmethod
    def get_transaction(transaction_id):
        """
        Retrieve a single transaction.
        """

        try:
            transaction = (
                InventoryTransaction.objects
                .select_related(
                    "inventory",
                    "inventory__product",
                    "created_by",
                )
                .get(id=transaction_id)
            )

            return {
                "success": True,
                "message": "Transaction found.",
                "data": transaction,
            }

        except InventoryTransaction.DoesNotExist:
            return {
                "success": False,
                "message": "Transaction not found.",
                "data": None,
            }

    @staticmethod
    def get_product_transactions(product_id):
        """
        Retrieve transaction history for a product.
        """

        transactions = (
            InventoryTransaction.objects
            .select_related(
                "inventory",
                "inventory__product",
                "created_by",
            )
            .filter(inventory__product_id=product_id)
        )

        return {
            "success": True,
            "message": "Transaction history retrieved successfully.",
            "data": transactions,
        }

    @staticmethod
    def get_transactions_by_type(transaction_type):
        """
        Retrieve transactions by type.
        """

        transactions = (
            InventoryTransaction.objects
            .select_related(
                "inventory",
                "inventory__product",
                "created_by",
            )
            .filter(transaction_type=transaction_type)
        )

        return {
            "success": True,
            "message": "Transactions retrieved successfully.",
            "data": transactions,
        }

    @staticmethod
    def delete_transaction(transaction):
        """
        Delete a transaction.
        """

        transaction.delete()

        return {
            "success": True,
            "message": "Transaction deleted successfully.",
        }