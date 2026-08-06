from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    # Authentication & Users
    path("api/users/", include("users.urls")),

    # Categories
    path("api/categories/", include("categories.urls")),

    # Products
    path("api/products/", include("products.urls")),

    # Inventory
    path("api/inventory/", include("inventory.urls")),

    #customers
    path("api/customers/",include("customers.urls")),

    #orders
    path("api/orders/",include("orders.urls")),

    #payments
    path("api/payments/",include("payments.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )