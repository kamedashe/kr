
from dataclasses import dataclass
from typing import Optional

@dataclass
class Storekeeper:
    name: str
    warehouse_id: int
    id: Optional[int] = None

    def __str__(self) -> str:
        return f"{self.name} (Склад ID: {self.warehouse_id})"

    def validate(self) -> bool:
        return bool(self.name.strip() and isinstance(self.warehouse_id, int))
