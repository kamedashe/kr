import sqlite3

class SupplierDAO:
    """SQLite DAO for suppliers using dict-based DTOs."""

    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self._create_table()

    def _create_table(self) -> None:
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS suppliers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                contact_info TEXT
            )
            """
        )
        self.conn.commit()

    def insert(self, supplier: dict) -> int:
        """Insert supplier and return new ID."""
        with self.conn:
            cur = self.conn.execute(
                "INSERT INTO suppliers (name, contact_info) VALUES (?, ?)",
                (supplier.get("name"), supplier.get("contact_info")),
            )
        return cur.lastrowid

    def update(self, supplier: dict) -> bool:
        """Update supplier by ID using dict fields."""
        with self.conn:
            cur = self.conn.execute(
                "UPDATE suppliers SET name = ?, contact_info = ? WHERE id = ?",
                (
                    supplier.get("name"),
                    supplier.get("contact_info"),
                    supplier.get("id"),
                ),
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

    def select_by_id(self, supplier_id: int) -> dict | None:
        cur = self.conn.execute(
            "SELECT id, name, contact_info FROM suppliers WHERE id = ?",
            (supplier_id,),
        )
        row = cur.fetchone()
        if row:
            return {"id": row[0], "name": row[1], "contact_info": row[2]}
        return None

    def select_all(self) -> list[dict]:
        cur = self.conn.execute(
            "SELECT id, name, contact_info FROM suppliers ORDER BY name"
        )
        return [
            {"id": r[0], "name": r[1], "contact_info": r[2]}
            for r in cur.fetchall()
        ]

    def select_by_name(self, name_substring: str) -> list[dict]:
        pattern = f"%{name_substring}%"
        cur = self.conn.execute(
            "SELECT id, name, contact_info FROM suppliers WHERE name LIKE ? ORDER BY name",
            (pattern,),
        )
        return [
            {"id": r[0], "name": r[1], "contact_info": r[2]}
            for r in cur.fetchall()
        ]
