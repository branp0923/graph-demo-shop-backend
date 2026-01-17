from app.models import LineItem
from app.services import charge_payment, create_order


def create_checkout(order_id: str, user_id: str, items_payload: list[dict]) -> dict:
    items = [LineItem(**payload) for payload in items_payload]
    order = create_order(order_id=order_id, user_id=user_id, items=items)
    payment = charge_payment(order)
    return {"order_id": order.order_id, "amount_cents": payment.amount_cents}
