from django.urls import path

from .views import (
    CustomerListCreateView,
    CustomerDetailView,
    AddressListCreateView,
    AddressDetailView,
)

urlpatterns = [

    path(
        "",
        CustomerListCreateView.as_view(),
        name="customer-list-create",
    ),

    path(
        "<int:pk>/",
        CustomerDetailView.as_view(),
        name="customer-detail",
    ),

    path(
        "addresses/",
        AddressListCreateView.as_view(),
        name="address-list-create",
    ),

    path(
        "addresses/<int:pk>/",
        AddressDetailView.as_view(),
        name="address-detail",
    ),
]