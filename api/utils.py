import random
import datetime as dt
from dataclasses import dataclass


@dataclass
class SyntheticSalesEntry:
    item_id: int
    sale_date: str
    sale_person_id: int
    sale_qty: int
    base_price: int
    discount_pct: int

    def __post_init__(self):
        self.final_price = self.base_price * (100 - self.discount_pct) / 100
        self.sale_price_total = self.final_price * self.sale_qty

    def to_json(self):
        return {
            'sale_date': self.item_id,
            'item_id': self.item_id,
            'qty': self.sale_qty,
            'base_price': self.base_price,
            'discount_pct': self.discount_pct,
            'final_price': self.final_price,
            'sale_price_total': self.sale_price_total,
            'sales_person_id': self.sale_person_id,
        }

    @classmethod
    def generate(cls):
        items = {
            101909: {'bp': [100, 105], 'dc': [10, 12], 'qt': [1, 20]},
            444909: {'bp': [500, 550], 'dc': [10, 12], 'qt': [1, 10]},
            101555: {'bp': [15000, 17000], 'dc': [0, 5], 'qt': [1, 3]},
            303303: {'bp': [5, 10], 'dc': [0, 2], 'qt': [1, 200]},
            408192: {'bp': [1800, 1820], 'dc': [0, 5], 'qt': [1, 5]},
            993241: {'bp': [2000, 2500], 'dc': [0, 5], 'qt': [1, 3]},
            953990: {'bp': [30, 40], 'dc': [0, 1], 'qt': [1, 20]},
            230054: {'bp': [100, 1000], 'dc': [10, 12], 'qt': [1, 20]},
            120304: {'bp': [20, 22], 'dc': [20, 30], 'qt': [1, 100]},
            121212: {'bp': [300, 350], 'dc': [0, 2], 'qt': [1, 10]},
            355342: {'bp': [400, 1500], 'dc': [20, 50], 'qt': [1, 10]},
        }
        sale_person = random.randint(10000, 10020)
        item_id, generators = random.choice(list(items.items()))

        return cls(
            item_id=item_id,
            sale_date=dt.date.today().isoformat(),
            sale_person_id=sale_person,
            sale_qty=random.randint(*generators['qt']),
            base_price=random.randint(*generators['bp']),
            discount_pct=random.randint(*generators['dc'])
        )


def generate_sales_entry():
    return SyntheticSalesEntry.generate().to_json()
