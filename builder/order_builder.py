from models.order import Order
from models.supply_record import SupplyRecord

class OrderBuilder:
    def __init__(self):
        self.order = Order()

    def add_item(self, component_id: int, quantity: int, price: float):
        record = SupplyRecord(
            supply_id=None,  # бо замовлення ще не оформлене
            component_id=component_id,
            quantity=quantity,
            price=price
        )
        self.order.add_item(record)
        return self  # щоб можна було ланцюжком викликати

    def build(self) -> Order:
        return self.order
