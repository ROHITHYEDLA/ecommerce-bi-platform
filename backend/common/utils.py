from datetime import date

from orders.models import Order


def generate_order_number():

    today = date.today().strftime("%Y%m%d")

    last_order = (
        Order.objects
        .filter(order_number__startswith=f"ORD-{today}")
        .order_by("-id")
        .first()
    )

    if last_order:

        last = int(last_order.order_number.split("-")[-1]) + 1

    else:

        last = 1

    return f"ORD-{today}-{last:06d}"