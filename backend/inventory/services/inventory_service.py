from inventory.models import Inventory


class InventoryService:

    @staticmethod
    def get_all_inventory():
        """
        Retrieve all inventory records.
        """
        inventory = Inventory.objects.select_related("product").all()

        return {
            "success": True,
            "message": "Inventory retrieved successfully.",
            "data": inventory,
        }

    @staticmethod
    def get_inventory(product_id):
        """
        Retrieve inventory for a specific product.
        """
        try:
            inventory = Inventory.objects.select_related("product").get(
                product_id=product_id
            )

            return {
                "success": True,
                "message": "Inventory found.",
                "data": inventory,
            }

        except Inventory.DoesNotExist:
            return {
                "success": False,
                "message": "Inventory not found.",
                "data": None,
            }

    @staticmethod
    def update_inventory(inventory, validated_data):
        """
        Update inventory settings only.
        Stock values are managed by StockService.
        """

        inventory.warehouse = validated_data.get(
            "warehouse",
            inventory.warehouse,
        )

        inventory.minimum_stock = validated_data.get(
            "minimum_stock",
            inventory.minimum_stock,
        )

        inventory.reorder_level = validated_data.get(
            "reorder_level",
            inventory.reorder_level,
        )

        inventory.maximum_stock = validated_data.get(
            "maximum_stock",
            inventory.maximum_stock,
        )

        inventory.save()

        return {
            "success": True,
            "message": "Inventory updated successfully.",
            "data": inventory,
        }

    @staticmethod
    def delete_inventory(inventory):
        """
        Delete an inventory record.
        """

        inventory.delete()

        return {
            "success": True,
            "message": "Inventory deleted successfully.",
        }