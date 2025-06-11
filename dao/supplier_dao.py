import sqlite3
from typing import List, Dict, Any


class SupplierDAO:
    """Data access object for suppliers."""

    def __init__(self, conn: sqlite3.Connection) -> None:
        self.conn = conn
        self._ensure_table()

    def _ensure_table(self) -> None:
        """Create suppliers table if missing."""
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS suppliers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                contact TEXT
            )
            """
        )
        self.conn.commit()

    def insert(self, supplier: Dict[str, Any]) -> int:
        """Insert a supplier and return its new ID."""
        with self.conn:
            cur = self.conn.execute(
                "INSERT INTO suppliers (name, contact) VALUES (?, ?)",
                (supplier.get("name"), supplier.get("contact")),
            )
        return cur.lastrowid

    def update(self, supplier_id: int, values: Dict[str, Any]) -> bool:
        """Update supplier identified by ``supplier_id``."""
        with self.conn:
            cur = self.conn.execute(
                "UPDATE suppliers SET name = ?, contact = ? WHERE id = ?",
                (values.get("name"), values.get("contact"), supplier_id),
            )
        return cur.rowcount > 0

    def delete(self, supplier_id: int) -> bool:
        """Delete supplier by ID."""
        with self.conn:
            cur = self.conn.execute(
                "DELETE FROM suppliers WHERE id = ?",
                (supplier_id,),
            )
        return cur.rowcount > 0

    def get(self, supplier_id: int) -> Dict[str, Any] | None:
        """Return supplier row by ID."""
        cur = self.conn.execute(
            "SELECT id, name, contact FROM suppliers WHERE id = ?",
            (supplier_id,),
        )
        row = cur.fetchone()
        if row:
            return {"id": row[0], "name": row[1], "contact": row[2]}
        return None

    def get_all(self) -> List[Dict[str, Any]]:
        """Return all suppliers ordered by ID."""
        cur = self.conn.execute(
            "SELECT id, name, contact FROM suppliers ORDER BY id"
        )
        return [{"id": r[0], "name": r[1], "contact": r[2]} for r in cur.fetchall()]
