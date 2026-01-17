from app.reports import estimate_cart_revenue
from app.models import LineItem


def main() -> None:
    items = [LineItem(sku="SKU-CLI", quantity=1, unit_cents=2500)]
    print(estimate_cart_revenue(items))


if __name__ == "__main__":
    main()
