from django.db import models

from uuid import uuid4


class PurchaseOrder(models.Model):

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("RECEIVED", "Received"),
        ("CANCELLED", "Cancelled"),
    ]

    supplier = models.ForeignKey(
        "suppliers.Supplier",
        on_delete=models.CASCADE,
        related_name="purchase_orders",
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING",
    )

    expected_delivery = models.DateField()

    received_date = models.DateField(
        null=True,
        blank=True,
    )

    po_number = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
    )

    remarks = models.TextField(
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"PO-{self.id}"

    def save(self, *args, **kwargs):
    
        if not self.po_number:
            self.po_number = (
                f"PO-{uuid4().hex[:8].upper()}"
            )
    
        super().save(*args, **kwargs)

class PurchaseOrderItem(models.Model):

    purchase_order = models.ForeignKey(
        PurchaseOrder,
        on_delete=models.CASCADE,
        related_name="items",
    )

    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        related_name="purchase_order_items",
    )

    quantity = models.PositiveIntegerField()

    unit_cost = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    total_cost = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    class Meta:
        ordering = ["id"]

    def save(self, *args, **kwargs):

        self.total_cost = self.quantity * self.unit_cost

        super().save(*args, **kwargs)

    def __str__(self):
        return self.product.name
