
from dataclasses import dataclass
from typing import Optional

@dataclass
class SupplyRecord:
    supply_id: int
    component_id: int
    quantity: int
    price: float
    id: Optional[int] = None

    def get_line_cost(self) -> float:
        return self.quantity * self.price

    def __str__(self) -> str:
        return f"Компонент {self.component_id} x {self.quantity} за {self.price}"
