from django.urls import path

from .views import (
    InventoryListCreateView,
    InventoryDetailView,
    InventoryTransactionCreateView,
)

urlpatterns = [
    path(
        "",
        InventoryListCreateView.as_view(),
        name="inventory-list-create",
    ),
    path(
        "<int:pk>/",
        InventoryDetailView.as_view(),
        name="inventory-detail",
    ),
    path(
        "transactions/",
        InventoryTransactionCreateView.as_view(),
        name="inventory-transaction-create",
    ),
]