from app.api import create_checkout


def test_create_checkout_amount():
    result = create_checkout(
        order_id="ord_test",
        user_id="user_test",
        items_payload=[{"sku": "SKU-T", "quantity": 1, "unit_cents": 1000}],
    )
    assert result["amount_cents"] > 0
