from app.api import create_checkout


def run_demo() -> dict:
    return create_checkout(
        order_id="ord_001",
        user_id="user_123",
        items_payload=[{"sku": "SKU-1", "quantity": 2, "unit_cents": 1500}],
    )


if __name__ == "__main__":
    print(run_demo())
