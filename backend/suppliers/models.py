from django.db import models


class Supplier(models.Model):

    company_name = models.CharField(
        max_length=255,
        unique=True,
    )

    contact_person = models.CharField(
        max_length=255,
    )

    email = models.EmailField(
        unique=True,
    )

    phone_number = models.CharField(
        max_length=20,
    )

    address = models.TextField()

    gst_number = models.CharField(
        max_length=20,
        unique=True,
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
        ordering = ["company_name"]

    def __str__(self):
        return self.company_name