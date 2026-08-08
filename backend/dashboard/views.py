from django.db.models import Sum, F

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from orders.models import Order
from customers.models import Customer
from inventory.models import Inventory
from products.models import Product
from procurement.models import PurchaseOrder, PurchaseOrderItem


class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        # -----------------------------
        # SALES
        # -----------------------------
        total_sales = (
            Order.objects.filter(
                status__in=[
                    "CONFIRMED",
                    "PROCESSING",
                    "SHIPPED",
                    "DELIVERED",
                ]
            )
            .aggregate(total=Sum("total_amount"))["total"]
            or 0
        )

        total_orders = Order.objects.count()

        pending_orders = Order.objects.filter(
            status="PENDING"
        ).count()

        delivered_orders = Order.objects.filter(
            status="DELIVERED"
        ).count()

        cancelled_orders = Order.objects.filter(
            status="CANCELLED"
        ).count()

        # -----------------------------
        # CUSTOMERS
        # -----------------------------
        total_customers = Customer.objects.count()

        active_customers = Customer.objects.filter(
            is_active=True
        ).count()

        # -----------------------------
        # PRODUCTS
        # -----------------------------
        total_products = Product.objects.count()

        active_products = Product.objects.filter(
            is_active=True
        ).count()

        # -----------------------------
        # INVENTORY
        # -----------------------------
        total_inventory_units = (
            Inventory.objects.aggregate(
                total=Sum("current_stock")
            )["total"]
            or 0
        )

        low_stock_count = Inventory.objects.filter(
            current_stock__lte=F("reorder_level")
        ).count()

        out_of_stock_count = Inventory.objects.filter(
            current_stock=0
        ).count()

        inventory_value = sum(
            item.current_stock * item.product.cost_price
            for item in Inventory.objects.select_related("product")
        )

        # -----------------------------
        # PROCUREMENT
        # -----------------------------
        total_purchase_orders = PurchaseOrder.objects.count()

        pending_purchase_orders = PurchaseOrder.objects.filter(
            status="PENDING"
        ).count()

        received_purchase_orders = PurchaseOrder.objects.filter(
            status="RECEIVED"
        ).count()

        cancelled_purchase_orders = PurchaseOrder.objects.filter(
            status="CANCELLED"
        ).count()

        procurement_value = (
            PurchaseOrderItem.objects.filter(
                purchase_order__status__in=[
                    "PENDING",
                    "RECEIVED",
                ]
            )
            .aggregate(total=Sum("total_cost"))["total"]
            or 0
        )

        # -----------------------------
        # RECENT ORDERS
        # -----------------------------
        recent_orders = []

        orders = (
            Order.objects
            .select_related("customer__user")
            .order_by("-created_at")[:5]
        )

        for order in orders:

            user = order.customer.user

            customer_name = (
                f"{user.first_name} {user.last_name}"
            ).strip()

            if not customer_name:
                customer_name = user.email

            recent_orders.append({
                "id": order.id,
                "order_number": order.order_number,
                "customer": customer_name,
                "status": order.status,
                "total_amount": str(order.total_amount),
                "created_at": order.created_at,
            })

        # -----------------------------
        # LOW STOCK PRODUCTS
        # -----------------------------
        low_stock_products = []

        inventory_items = (
            Inventory.objects
            .filter(current_stock__lte=F("reorder_level"))
            .select_related("product")
            .order_by("current_stock")[:10]
        )

        for item in inventory_items:

            low_stock_products.append({
                "product_id": item.product.id,
                "product": item.product.name,
                "current_stock": item.current_stock,
                "reorder_level": item.reorder_level,
                "minimum_stock": item.minimum_stock,
            })

        # -----------------------------
        # RESPONSE
        # -----------------------------
        return Response({

            "sales": {
                "total_sales": str(total_sales),
                "total_orders": total_orders,
                "pending_orders": pending_orders,
                "delivered_orders": delivered_orders,
                "cancelled_orders": cancelled_orders,
            },

            "customers": {
                "total": total_customers,
                "active": active_customers,
            },

            "products": {
                "total": total_products,
                "active": active_products,
            },

            "inventory": {
                "total_units": total_inventory_units,
                "inventory_value": str(inventory_value),
                "low_stock": low_stock_count,
                "out_of_stock": out_of_stock_count,
            },

            "procurement": {
                "total_purchase_orders": total_purchase_orders,
                "pending": pending_purchase_orders,
                "received": received_purchase_orders,
                "cancelled": cancelled_purchase_orders,
                "total_value": str(procurement_value),
            },

            "recent_orders": recent_orders,

            "low_stock_products": low_stock_products,
        })