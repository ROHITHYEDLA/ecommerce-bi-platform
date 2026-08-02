from django.db import models
from django.utils.text import slugify

from categories.models import Category


class Product(models.Model):

    name = models.CharField(
        max_length=255,
        unique=True,
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
    )

    description = models.TextField(
        blank=True,
    )

    brand = models.CharField(
        max_length=100,
    )

    sku = models.CharField(
        max_length=100,
        unique=True,
    )

    barcode = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    cost_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    selling_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    stock_quantity = models.PositiveIntegerField(
        default=0,
    )

    minimum_stock = models.PositiveIntegerField(
        default=10,
    )

    weight = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True,
    )

    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name