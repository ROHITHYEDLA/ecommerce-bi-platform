from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from orders.models import Order

from .permissions import IsAdminUserRole
from .serializers import (
    PaymentCreateSerializer,
    PaymentSerializer,
)
from .services import (
    PaymentProcessor,
    PaymentService,
)


class PaymentCreateView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsAdminUserRole,
    ]

    def post(self, request):

        serializer = PaymentCreateSerializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        order = get_object_or_404(
            Order,
            pk=serializer.validated_data["order"],
        )

        payment = PaymentProcessor.process_payment(
            order=order,
            payment_method=serializer.validated_data["payment_method"],
            remarks=serializer.validated_data.get(
                "remarks",
                "",
            ),
        )

        return Response(
            PaymentSerializer(payment).data,
            status=status.HTTP_201_CREATED,
        )


class PaymentListView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsAdminUserRole,
    ]

    def get(self, request):

        payments = PaymentService.list_payments()

        serializer = PaymentSerializer(
            payments,
            many=True,
        )

        return Response(serializer.data)