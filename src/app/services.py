from typing import List

from app.config import DEFAULT_CURRENCY, TAX_RATE
from app.models import LineItem, Order, Payment
from app.jobs import enqueue_receipt_email


def calculate_total(items: List[LineItem]) -> int:
    subtotal = sum(item.quantity * item.unit_cents for item in items)
    tax = int(subtotal * TAX_RATE)
    return subtotal + tax


def create_order(order_id: str, user_id: str, items: List[LineItem]) -> Order:
    total_cents = calculate_total(items)
    return Order(order_id=order_id, user_id=user_id, items=items, total_cents=total_cents)


def charge_payment(order: Order) -> Payment:
    payment = Payment(order_id=order.order_id, amount_cents=order.total_cents, currency=DEFAULT_CURRENCY)
    enqueue_receipt_email(order.order_id)
    return payment
