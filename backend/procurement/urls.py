from django.urls import path

from .views import *

urlpatterns = [

    path(
        "",
        PurchaseOrderListCreateView.as_view(),
    ),

    path(
        "<int:pk>/",
        PurchaseOrderDetailView.as_view(),
    ),

    path(
        "items/",
        PurchaseOrderItemListCreateView.as_view(),
    ),

    path(
        "items/<int:pk>/",
        PurchaseOrderItemDetailView.as_view(),
    ),

    path(
        "<int:pk>/receive/",
        ReceivePurchaseOrderView.as_view(),
    ),
]