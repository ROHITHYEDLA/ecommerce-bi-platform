from django.db import models


class Inventory(models.Model):
    product = models.OneToOneField(
        "products.Product",
        on_delete=models.CASCADE,
        related_name="inventory",
    )

    warehouse = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    current_stock = models.PositiveIntegerField(default=0)

    reserved_stock = models.PositiveIntegerField(default=0)

    minimum_stock = models.PositiveIntegerField(default=5)

    reorder_level = models.PositiveIntegerField(default=10)

    maximum_stock = models.PositiveIntegerField(default=1000)

    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["product__name"]
        verbose_name = "Inventory"
        verbose_name_plural = "Inventory"

    def __str__(self):
        return f"{self.product.name} Inventory"

    @property
    def available_stock(self):
        return self.current_stock - self.reserved_stock




class InventoryTransaction(models.Model):

    TRANSACTION_TYPES = [
        ("STOCK_IN", "Stock In"),
        ("STOCK_OUT", "Stock Out"),
        ("RETURN", "Return"),
        ("DAMAGE", "Damage"),
        ("ADJUSTMENT", "Adjustment"),
    ]

    inventory = models.ForeignKey(
        Inventory,
        on_delete=models.CASCADE,
        related_name="transactions",
    )

    transaction_type = models.CharField(
        max_length=20,
        choices=TRANSACTION_TYPES,
    )

    quantity = models.PositiveIntegerField()

    reference = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    remarks = models.TextField(
        blank=True,
        null=True,
    )

    created_by = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Inventory Transaction"
        verbose_name_plural = "Inventory Transactions"

    def __str__(self):
        return (
            f"{self.inventory.product.name} - "
            f"{self.transaction_type} ({self.quantity})"
        )