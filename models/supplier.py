
from dataclasses import dataclass
from typing import Optional

@dataclass
class Supplier:
    name: str
    contact_info: str = ""
    id: Optional[int] = None

    def get_details(self) -> str:
        return f"Постачальник: {self.name}, Контакт: {self.contact_info}"

    def validate(self) -> bool:
        return bool(self.name.strip())
