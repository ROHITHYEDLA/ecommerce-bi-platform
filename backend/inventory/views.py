from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Inventory
from .permissions import IsAdminUserRole
from .serializers import (
    InventorySerializer,
    InventoryTransactionSerializer,
)
from .services import (
    InventoryService,
    TransactionService,
)


class InventoryListCreateView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsAdminUserRole,
    ]

    def get(self, request):
        inventory = InventoryService.list_inventory()
        serializer = InventorySerializer(
            inventory,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = InventorySerializer(data=request.data)

        if serializer.is_valid():
            inventory = InventoryService.create_inventory(
                **serializer.validated_data
            )

            return Response(
                InventorySerializer(inventory).data,
                status=status.HTTP_201_CREATED,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class InventoryDetailView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsAdminUserRole,
    ]

    def get(self, request, pk):
        inventory = InventoryService.get_inventory(pk)

        return Response(
            InventorySerializer(inventory).data
        )

    def put(self, request, pk):
        inventory = InventoryService.get_inventory(pk)

        serializer = InventorySerializer(
            inventory,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():

            inventory = InventoryService.update_inventory(
                inventory,
                **serializer.validated_data
            )

            return Response(
                InventorySerializer(inventory).data
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, pk):
        inventory = InventoryService.get_inventory(pk)

        InventoryService.delete_inventory(inventory)

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )


class InventoryTransactionCreateView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsAdminUserRole,
    ]

    def post(self, request):

        serializer = InventoryTransactionSerializer(
            data=request.data
        )

        if serializer.is_valid():

            transaction = TransactionService.create_transaction(
                inventory=serializer.validated_data["inventory"],
                transaction_type=serializer.validated_data["transaction_type"],
                quantity=serializer.validated_data["quantity"],
                created_by=request.user,
                reference=serializer.validated_data.get(
                    "reference",
                    "",
                ),
                remarks=serializer.validated_data.get(
                    "remarks",
                    "",
                ),
            )

            return Response(
                InventorySerializer(transaction).data,
                status=status.HTTP_201_CREATED,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )