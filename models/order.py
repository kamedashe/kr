from dataclasses import dataclass, field
from typing import List
from .supply_record import SupplyRecord

@dataclass
class Order:
    items: List[SupplyRecord] = field(default_factory=list)

    def add_item(self, record: SupplyRecord) -> None:
        self.items.append(record)

    def calculate_total(self) -> float:
        return sum(item.get_line_cost() for item in self.items)

    def __str__(self) -> str:
        lines = ["=== Замовлення ==="]
        for i, item in enumerate(self.items, 1):
            lines.append(
                f"{i}) Компонент ID: {item.component_id}, Кількість: {item.quantity}, Ціна: {item.price}"
            )
        lines.append(f"Загальна вартість: {self.calculate_total():.2f}")
        return "\n".join(lines)
