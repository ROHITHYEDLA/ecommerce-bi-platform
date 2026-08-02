from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import Category
from .serializers import CategorySerializer
from .permissions import IsAdminOrReadOnly
from .services import CategoryService


class CategoryListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    serializer_class = CategorySerializer

    def get_queryset(self):
        return CategoryService.get_all_categories()

    def perform_create(self, serializer):
        CategoryService.create_category(serializer.validated_data)


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    serializer_class = CategorySerializer

    def get_object(self):
        return get_object_or_404(
            Category,
            pk=self.kwargs["pk"]
        )

    def perform_update(self, serializer):
        CategoryService.update_category(
            serializer.instance,
            serializer.validated_data,
        )

    def perform_destroy(self, instance):
        CategoryService.delete_category(instance)