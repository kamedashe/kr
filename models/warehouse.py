
from dataclasses import dataclass
from typing import Optional

@dataclass
class Warehouse:
    name: str
    location: str
    id: Optional[int] = None

    def __str__(self) -> str:
        return f"{self.name} ({self.location})"

    def validate(self) -> bool:
        return bool(self.name.strip() and self.location.strip())
