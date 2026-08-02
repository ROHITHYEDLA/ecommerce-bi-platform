from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category

        fields = [
            "id",
            "name",
            "slug",
            "description",
            "image",
            "is_active",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "slug",
            "created_at",
            "updated_at",
        ]

    def validate_name(self, value):
        value = value.strip()

        if Category.objects.filter(name__iexact=value).exists():
            raise serializers.ValidationError(
                "Category with this name already exists."
            )

        return value