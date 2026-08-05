from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Inventory, InventoryTransaction
from .permissions import IsAdminOrReadOnly
from .serializers import (
    InventorySerializer,
    InventoryTransactionSerializer,
)
from .services.inventory_service import InventoryService
from .services.stock_service import StockService
from .services.transaction_service import TransactionService


class InventoryListView(generics.ListAPIView):

    queryset = Inventory.objects.select_related("product").all()
    serializer_class = InventorySerializer
    permission_classes = [IsAdminOrReadOnly]


class InventoryDetailView(generics.RetrieveUpdateAPIView):

    queryset = Inventory.objects.select_related("product").all()
    serializer_class = InventorySerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_update(self, serializer):
        InventoryService.update_inventory(serializer)


class StockInView(APIView):

    permission_classes = [IsAdminOrReadOnly]

    def post(self, request, pk):

        inventory = generics.get_object_or_404(
            Inventory,
            pk=pk,
        )

        quantity = int(request.data.get("quantity", 0))

        result = StockService.add_stock(
            inventory=inventory,
            quantity=quantity,
            user=request.user,
            reference=request.data.get("reference"),
            remarks=request.data.get("remarks"),
        )

        status_code = (
            status.HTTP_200_OK
            if result["success"]
            else status.HTTP_400_BAD_REQUEST
        )

        return Response(result, status=status_code)


class StockOutView(APIView):

    permission_classes = [IsAdminOrReadOnly]

    def post(self, request, pk):

        inventory = generics.get_object_or_404(
            Inventory,
            pk=pk,
        )

        quantity = int(request.data.get("quantity", 0))

        result = StockService.remove_stock(
            inventory=inventory,
            quantity=quantity,
            user=request.user,
            reference=request.data.get("reference"),
            remarks=request.data.get("remarks"),
        )

        status_code = (
            status.HTTP_200_OK
            if result["success"]
            else status.HTTP_400_BAD_REQUEST
        )

        return Response(result, status=status_code)


class ReserveStockView(APIView):

    permission_classes = [IsAdminOrReadOnly]

    def post(self, request, pk):

        inventory = generics.get_object_or_404(
            Inventory,
            pk=pk,
        )

        quantity = int(request.data.get("quantity", 0))

        result = StockService.reserve_stock(
            inventory=inventory,
            quantity=quantity,
        )

        status_code = (
            status.HTTP_200_OK
            if result["success"]
            else status.HTTP_400_BAD_REQUEST
        )

        return Response(result, status=status_code)


class ReleaseReservedStockView(APIView):

    permission_classes = [IsAdminOrReadOnly]

    def post(self, request, pk):

        inventory = generics.get_object_or_404(
            Inventory,
            pk=pk,
        )

        quantity = int(request.data.get("quantity", 0))

        result = StockService.release_reserved_stock(
            inventory=inventory,
            quantity=quantity,
        )

        status_code = (
            status.HTTP_200_OK
            if result["success"]
            else status.HTTP_400_BAD_REQUEST
        )

        return Response(result, status=status_code)


class TransactionListView(generics.ListAPIView):

    queryset = (
        InventoryTransaction.objects
        .select_related(
            "inventory",
            "inventory__product",
            "created_by",
        )
        .all()
    )

    serializer_class = InventoryTransactionSerializer
    permission_classes = [IsAdminOrReadOnly]


class TransactionDetailView(generics.RetrieveAPIView):

    queryset = (
        InventoryTransaction.objects
        .select_related(
            "inventory",
            "inventory__product",
            "created_by",
        )
        .all()
    )

    serializer_class = InventoryTransactionSerializer
    permission_classes = [IsAdminOrReadOnly]