from django.shortcuts import get_object_or_404

from payments.models import Payment


class PaymentService:

    @staticmethod
    def create_payment(**data):
        return Payment.objects.create(**data)

    @staticmethod
    def get_payment(payment_id):
        return get_object_or_404(
            Payment,
            pk=payment_id,
        )

    @staticmethod
    def list_payments():
        return Payment.objects.select_related(
            "order",
            "order__customer",
            "order__customer__user",
        )

    @staticmethod
    def update_payment(payment, **data):

        for field, value in data.items():
            setattr(payment, field, value)

        payment.save()

        return payment