import sqlite3
from models.warehouse import Warehouse

class WarehouseDAO:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.create_table()

    def create_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS warehouses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                location TEXT
            )
        """)
        self.conn.commit()

    def insert(self, wh: Warehouse) -> int:
        with self.conn:
            cursor = self.conn.execute(
                "INSERT INTO warehouses (name, location) VALUES (?, ?)",
                (wh.name, wh.location)
            )
        wh.id = cursor.lastrowid
        return wh.id

    def update(self, wh: Warehouse) -> bool:
        with self.conn:
            cursor = self.conn.execute(
                "UPDATE warehouses SET name = ?, location = ? WHERE id = ?",
                (wh.name, wh.location, wh.id)
            )
        return cursor.rowcount > 0

    def delete(self, wh_id: int) -> bool:
        with self.conn:
            cursor = self.conn.execute(
                "DELETE FROM warehouses WHERE id = ?",
                (wh_id,)
            )
        return cursor.rowcount > 0

    def find_by_id(self, wh_id: int) -> Warehouse | None:
        cursor = self.conn.execute(
            "SELECT id, name, location FROM warehouses WHERE id = ?",
            (wh_id,)
        )
        row = cursor.fetchone()
        if not row:
            return None
        return Warehouse(id=row[0], name=row[1], location=row[2])

    def find_all(self) -> list[Warehouse]:
        cursor = self.conn.execute(
            "SELECT id, name, location FROM warehouses ORDER BY name"
        )
        return [Warehouse(id=r[0], name=r[1], location=r[2]) for r in cursor.fetchall()]