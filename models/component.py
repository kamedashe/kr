
from dataclasses import dataclass
from typing import Optional

@dataclass
class Component:
    name: str
    unit: str
    quantity_in_stock: int = 0
    id: Optional[int] = None

    def get_info(self) -> str:
        return f"{self.name} ({self.unit}), на складі: {self.quantity_in_stock}"

    def validate(self) -> bool:
        return bool(self.name.strip() and self.unit.strip())
