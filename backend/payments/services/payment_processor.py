from uuid import uuid4

from .payment_service import PaymentService

from rest_framework.exceptions import ValidationError



class PaymentProcessor:

    @staticmethod
    def process_payment(
        order,
        payment_method,
        remarks="",
    ):

        if hasattr(order, "payment"):
            raise ValidationError(
                "Payment already exists for this order."
            )

        transaction_id = f"TXN-{uuid4().hex[:12].upper()}"

        payment = PaymentService.create_payment(
            order=order,
            transaction_id=transaction_id,
            payment_method=payment_method,
            payment_status="SUCCESS",
            amount=order.total_amount,
            remarks=remarks,
        )

        order.status = "CONFIRMED"
        order.save(update_fields=["status"])

        return payment