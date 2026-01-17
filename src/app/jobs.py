from app.reports import record_revenue


def enqueue_receipt_email(order_id: str) -> None:
    # Placeholder for a real queue enqueue
    record_revenue(order_id)
