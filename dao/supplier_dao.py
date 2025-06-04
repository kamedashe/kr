import sqlite3
from models.supplier import Supplier

class SupplierDAO:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.create_table()

    def create_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS suppliers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                contact_info TEXT
            )
        """)
        self.conn.commit()

    def insert(self, supplier: Supplier) -> int:
        with self.conn:
            cursor = self.conn.execute(
                "INSERT INTO suppliers (name, contact_info) VALUES (?, ?)",
                (supplier.name, supplier.contact_info)
            )
        supplier.id = cursor.lastrowid
        return supplier.id

    def update(self, supplier: Supplier) -> bool:
        with self.conn:
            cursor = self.conn.execute(
                "UPDATE suppliers SET name = ?, contact_info = ? WHERE id = ?",
                (supplier.name, supplier.contact_info, supplier.id)
            )
        return cursor.rowcount > 0

    def delete(self, supplier_id: int) -> bool:
        with self.conn:
            cursor = self.conn.execute(
                "DELETE FROM suppliers WHERE id = ?",
                (supplier_id,)
            )
        return cursor.rowcount > 0

    def find_by_id(self, supplier_id: int) -> Supplier | None:
        cursor = self.conn.execute(
            "SELECT id, name, contact_info FROM suppliers WHERE id = ?",
            (supplier_id,)
        )
        row = cursor.fetchone()
        if not row:
            return None
        return Supplier(id=row[0], name=row[1], contact_info=row[2])

    def find_all(self) -> list[Supplier]:
        cursor = self.conn.execute(
            "SELECT id, name, contact_info FROM suppliers ORDER BY name"
        )
        return [Supplier(id=r[0], name=r[1], contact_info=r[2]) for r in cursor.fetchall()]

    def find_by_name(self, name_substring: str) -> list[Supplier]:
        pattern = f"%{name_substring}%"
        cursor = self.conn.execute(
            "SELECT id, name, contact_info FROM suppliers WHERE name LIKE ? ORDER BY name",
            (pattern,)
        )
        return [Supplier(id=r[0], name=r[1], contact_info=r[2]) for r in cursor.fetchall()]