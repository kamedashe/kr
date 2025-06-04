
from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class Supply:
    supply_date: date
    supplier_id: int
    warehouse_id: int
    storekeeper_id: int
    id: Optional[int] = None

    def __str__(self) -> str:
        return f"Поставка {self.id} від {self.supply_date}"
