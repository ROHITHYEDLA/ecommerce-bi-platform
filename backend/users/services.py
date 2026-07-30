from .models import User


class UserService:

    @staticmethod
    def create_user(validated_data):

        password = validated_data.pop("password")

        user = User.objects.create_user(
            email=validated_data["email"],
            username=validated_data["username"],
            password=password,
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            phone_number=validated_data["phone_number"],
            role=validated_data.get("role", "CUSTOMER"),
        )

        return user