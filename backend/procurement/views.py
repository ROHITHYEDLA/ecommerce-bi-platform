from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services.procurement_service import ProcurementService
from .models import PurchaseOrder
from .models import PurchaseOrderItem

from .serializers import (
    PurchaseOrderSerializer,
    PurchaseOrderItemSerializer,
)

from .permissions import IsAdminUserRole


class PurchaseOrderListCreateView(
    generics.ListCreateAPIView
):

    queryset = PurchaseOrder.objects.all()

    serializer_class = PurchaseOrderSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdminUserRole,
    ]


class PurchaseOrderDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    queryset = PurchaseOrder.objects.all()

    serializer_class = PurchaseOrderSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdminUserRole,
    ]


class PurchaseOrderItemListCreateView(
    generics.ListCreateAPIView
):

    queryset = PurchaseOrderItem.objects.all()

    serializer_class = PurchaseOrderItemSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdminUserRole,
    ]


class PurchaseOrderItemDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    queryset = PurchaseOrderItem.objects.all()

    serializer_class = PurchaseOrderItemSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdminUserRole,
    ]


class ReceivePurchaseOrderView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsAdminUserRole,
    ]

    def post(self, request, pk):

        purchase_order = PurchaseOrder.objects.get(pk=pk)

        ProcurementService.receive_purchase_order(
            purchase_order=purchase_order,
            received_by=request.user,
        )

        return Response(
            {
                "message": "Purchase Order received successfully."
            },
            status=status.HTTP_200_OK,
        )