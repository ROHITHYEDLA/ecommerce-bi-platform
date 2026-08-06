from django.shortcuts import get_object_or_404
from .permissions import IsAdminUserRole
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from customers.models import Customer
from products.models import Product

from .serializers import (
    CheckoutSerializer,
    OrderSerializer,
)
from .services import (
    CheckoutService,
    OrderService,
)


class CheckoutView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsAdminUserRole,
    ]

    def post(self, request):

        serializer = CheckoutSerializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        customer = get_object_or_404(
            Customer,
            pk=serializer.validated_data["customer"],
        )

        items = []

        for item in serializer.validated_data["items"]:

            product = get_object_or_404(
                Product,
                pk=item["product"],
            )

            items.append(
                {
                    "product": product,
                    "quantity": item["quantity"],
                }
            )

        order = CheckoutService.checkout(
            customer=customer,
            items=items,
            created_by=request.user,
        )

        return Response(
            OrderSerializer(order).data,
            status=status.HTTP_201_CREATED,
        )


class OrderListView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsAdminUserRole,
    ]

    def get(self, request):

        orders = OrderService.list_orders()

        serializer = OrderSerializer(
            orders,
            many=True,
        )

        return Response(serializer.data)