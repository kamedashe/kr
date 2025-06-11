import sqlite3
from typing import Any, Dict, List, Tuple


class OrderDAO:
    """DAO for purchase orders."""

    def __init__(self, conn: sqlite3.Connection) -> None:
        self.conn = conn
        self._ensure_table()

    def _ensure_table(self) -> None:
        """Create orders table if missing."""
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                supplier_id INTEGER NOT NULL,
                component_id INTEGER NOT NULL,
                qty INTEGER NOT NULL,
                date TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (supplier_id) REFERENCES suppliers(id),
                FOREIGN KEY (component_id) REFERENCES components(id)
            )
            """
        )
        self.conn.commit()

    def insert(self, supplier_id: int, component_id: int, qty: int) -> int:
        """Insert an order and update stock/history."""
        with self.conn:
            cur = self.conn.execute(
                "INSERT INTO orders (supplier_id, component_id, qty) VALUES (?, ?, ?)",
                (supplier_id, component_id, qty),
            )
            self.conn.execute(
                "UPDATE components SET quantity_in_stock = quantity_in_stock + ? WHERE id = ?",
                (qty, component_id),
            )
            self.conn.execute(
                "INSERT INTO supply_history (supplier_id, component_id, qty, date) VALUES (?, ?, ?, CURRENT_TIMESTAMP)",
                (supplier_id, component_id, qty),
            )
        return cur.lastrowid

    def list_all(self) -> List[Tuple[int, str, str, int, str]]:
        """Return all orders with human readable fields."""
        cur = self.conn.execute(
            """
            SELECT o.id, s.name, c.name, o.qty, o.date
              FROM orders o
              JOIN suppliers s ON o.supplier_id = s.id
              JOIN components c ON o.component_id = c.id
             ORDER BY o.id
            """
        )
        return [
            (row[0], row[1], row[2], row[3], row[4])
            for row in cur.fetchall()
        ]

    def get(self, order_id: int) -> Dict[str, Any] | None:
        """Return single order row with supplier and component names."""
        cur = self.conn.execute(
            """
            SELECT o.id, s.name, c.name, o.qty, o.date
              FROM orders o
              JOIN suppliers s ON o.supplier_id = s.id
              JOIN components c ON o.component_id = c.id
             WHERE o.id = ?
            """,
            (order_id,),
        )
        row = cur.fetchone()
        if row is None:
            return None
        return {
            "id": row[0],
            "supplier": row[1],
            "details": f"{row[2]} x {row[3]}",
            "date": row[4],
        }
