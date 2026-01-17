from dataclasses import dataclass
from typing import List


@dataclass
class LineItem:
    sku: str
    quantity: int
    unit_cents: int


@dataclass
class Order:
    order_id: str
    user_id: str
    items: List[LineItem]
    total_cents: int


@dataclass
class Payment:
    order_id: str
    amount_cents: int
    currency: str
