from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import User
from .services import UserService
from .validators import validate_phone, validate_password


class UserRegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        validators=[validate_password],
    )

    confirm_password = serializers.CharField(write_only=True)

    phone_number = serializers.CharField(
        validators=[validate_phone]
    )

    class Meta:
        model = User

        fields = [
            "email",
            "username",
            "first_name",
            "last_name",
            "phone_number",
            "role",
            "password",
            "confirm_password",
        ]

        extra_kwargs = {
            "role": {"required": False}
        }

    def validate(self, attrs):

        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {
                    "confirm_password": "Passwords do not match."
                }
            )

        return attrs

    def create(self, validated_data):

        validated_data.pop("confirm_password")

        return UserService.create_user(validated_data)




class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(
            username=email,
            password=password
        )

        if not user:
            raise serializers.ValidationError(
                "Invalid email or password."
            )

        attrs["user"] = user
        return attrs
class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "phone_number",
            "profile_image",
            "role",
            "date_joined",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "email",
            "role",
            "date_joined",
            "updated_at",
        ]