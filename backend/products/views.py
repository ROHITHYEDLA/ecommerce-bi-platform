from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer
from .services import ProductService
from .permissions import IsAdminOrReadOnly


class ProductListCreateView(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        ProductService.create_product(serializer)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_update(self, serializer):
        ProductService.update_product(serializer)

    def perform_destroy(self, instance):
        ProductService.delete_product(instance)