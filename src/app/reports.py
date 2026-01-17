from app.services import calculate_total
from app.models import LineItem


def record_revenue(order_id: str) -> None:
    # Stub for analytics pipeline
    _ = order_id


def estimate_cart_revenue(items: list[LineItem]) -> int:
    return calculate_total(items)
