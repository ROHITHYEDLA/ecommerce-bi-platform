from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import IsAdminUserRole
from .serializers import (
    CustomerSerializer,
    CustomerAddressSerializer,
)
from .services import (
    CustomerService,
    AddressService,
)


class CustomerListCreateView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsAdminUserRole,
    ]

    def get(self, request):
        customers = CustomerService.list_customers()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)

        if serializer.is_valid():
            customer = CustomerService.create_customer(
                **serializer.validated_data
            )

            return Response(
                CustomerSerializer(customer).data,
                status=status.HTTP_201_CREATED,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class CustomerDetailView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsAdminUserRole,
    ]

    def get(self, request, pk):
        customer = CustomerService.get_customer(pk)

        return Response(
            CustomerSerializer(customer).data
        )

    def put(self, request, pk):
        customer = CustomerService.get_customer(pk)

        serializer = CustomerSerializer(
            customer,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():
            customer = CustomerService.update_customer(
                customer,
                **serializer.validated_data,
            )

            return Response(
                CustomerSerializer(customer).data
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, pk):
        customer = CustomerService.delete_customer(
            CustomerService.get_customer(pk)
        )

        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )


class AddressListCreateView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsAdminUserRole,
    ]

    def get(self, request):
        addresses = AddressService.list_addresses()

        serializer = CustomerAddressSerializer(
            addresses,
            many=True,
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerAddressSerializer(
            data=request.data
        )

        if serializer.is_valid():

            address = AddressService.create_address(
                **serializer.validated_data
            )

            return Response(
                CustomerAddressSerializer(address).data,
                status=status.HTTP_201_CREATED,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class AddressDetailView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsAdminUserRole,
    ]

    def get(self, request, pk):

        address = AddressService.get_address(pk)

        return Response(
            CustomerAddressSerializer(address).data
        )

    def put(self, request, pk):

        address = AddressService.get_address(pk)

        serializer = CustomerAddressSerializer(
            address,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():

            address = AddressService.update_address(
                address,
                **serializer.validated_data,
            )

            return Response(
                CustomerAddressSerializer(address).data
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, pk):

        AddressService.delete_address(
            AddressService.get_address(pk)
        )

        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )