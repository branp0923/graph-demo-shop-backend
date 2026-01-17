from app.events import register
from app.services import calculate_total
from app.models import LineItem


def record_revenue(order_id: str) -> None:
    # Stub for analytics pipeline
    _ = order_id


def _on_payment_charged(payload: dict) -> None:
    _ = payload


register("payment_charged", _on_payment_charged)


def estimate_cart_revenue(items: list[LineItem]) -> int:
    return calculate_total(items)
