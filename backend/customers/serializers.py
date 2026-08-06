from rest_framework import serializers

from .models import Customer, CustomerAddress


class CustomerSerializer(serializers.ModelSerializer):

    email = serializers.CharField(
        source="user.email",
        read_only=True,
    )

    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = "__all__"

    def get_full_name(self, obj):
        first_name = getattr(obj.user, "first_name", "")
        last_name = getattr(obj.user, "last_name", "")

        full_name = f"{first_name} {last_name}".strip()

        return full_name if full_name else obj.user.email


class CustomerAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerAddress
        fields = "__all__"