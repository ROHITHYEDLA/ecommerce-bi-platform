from .models import Category


class CategoryService:

    @staticmethod
    def create_category(validated_data):
        return Category.objects.create(**validated_data)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    @staticmethod
    def get_category_by_id(category_id):
        return Category.objects.get(id=category_id)

    @staticmethod
    def update_category(category, validated_data):
        for key, value in validated_data.items():
            setattr(category, key, value)

        category.save()
        return category

    @staticmethod
    def delete_category(category):
        category.delete()