from django.urls import path

from .views import (
    PaymentCreateView,
    PaymentListView,
)

urlpatterns = [

    path(
        "",
        PaymentListView.as_view(),
        name="payments",
    ),

    path(
        "create/",
        PaymentCreateView.as_view(),
        name="create-payment",
    ),
]