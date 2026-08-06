from django.contrib import admin

from .models import Customer, CustomerAddress


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "phone_number",
        "loyalty_points",
        "is_active",
    )

    search_fields = (
        "user__email",
        "user__first_name",
        "user__last_name",
        "phone_number",
    )


@admin.register(CustomerAddress)
class CustomerAddressAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "customer",
        "address_type",
        "city",
        "state",
        "country",
        "is_default",
    )

    search_fields = (
        "customer__user__email",
        "city",
        "state",
    )