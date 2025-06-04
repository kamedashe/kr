
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Iterable, Mapping

class ExportStrategy(ABC):
    """Інтерфейс стратегії експорту (CSV, PDF …)."""

    @abstractmethod
    def export(self, rows: Iterable[Mapping], out_path: Path) -> Path:
        """Повертає шлях до створеного файла."""
