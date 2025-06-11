import sqlite3
from typing import List, Tuple
from dao.component_dao import ComponentDAO


class WarehouseDAO(ComponentDAO):
    """DAO providing warehouse specific operations."""

    def __init__(self, conn: sqlite3.Connection) -> None:
        super().__init__(conn)
        self._ensure_history_table()

    def _ensure_history_table(self) -> None:
        """Create ``supply_history`` table if missing."""
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS supply_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                supplier_id INTEGER,
                component_id INTEGER NOT NULL,
                qty INTEGER NOT NULL,
                date TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (supplier_id) REFERENCES suppliers(id),
                FOREIGN KEY (component_id) REFERENCES components(id)
            )
            """
        )
        self.conn.commit()

    def get_all_stock(self) -> List[Tuple[int, str, int]]:
        """Return list of component id, name and quantity."""
        cur = self.conn.execute(
            "SELECT id, name, quantity_in_stock FROM components ORDER BY id"
        )
        return [(row[0], row[1], row[2]) for row in cur.fetchall()]

    def register_expense(self, component_id: int, qty: int) -> None:
        """Write component usage to history and decrease stock."""
        cur = self.conn.execute(
            "SELECT quantity_in_stock FROM components WHERE id = ?",
            (component_id,),
        )
        row = cur.fetchone()
        if row is None:
            raise ValueError("Component not found")
        if qty > row[0]:
            raise ValueError("Insufficient stock")

        with self.conn:
            self.conn.execute(
                "UPDATE components SET quantity_in_stock = quantity_in_stock - ? WHERE id = ?",
                (qty, component_id),
            )
            self.conn.execute(
                "INSERT INTO supply_history (supplier_id, component_id, qty, date) VALUES (NULL, ?, ?, CURRENT_TIMESTAMP)",
                (component_id, -qty),
            )
