import sqlite3
from models.storekeeper import Storekeeper

class StorekeeperDAO:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.create_table()

    def create_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS storekeepers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                warehouse_id INTEGER,
                FOREIGN KEY (warehouse_id) REFERENCES warehouses(id)
            )
        """)
        self.conn.commit()

    def insert(self, keeper: Storekeeper) -> int:
        with self.conn:
            cursor = self.conn.execute(
                "INSERT INTO storekeepers (name, warehouse_id) VALUES (?, ?)",
                (keeper.name, keeper.warehouse_id)
            )
        keeper.id = cursor.lastrowid
        return keeper.id

    def update(self, keeper: Storekeeper) -> bool:
        with self.conn:
            cursor = self.conn.execute(
                "UPDATE storekeepers SET name = ?, warehouse_id = ? WHERE id = ?",
                (keeper.name, keeper.warehouse_id, keeper.id)
            )
        return cursor.rowcount > 0

    def delete(self, keeper_id: int) -> bool:
        with self.conn:
            cursor = self.conn.execute(
                "DELETE FROM storekeepers WHERE id = ?",
                (keeper_id,)
            )
        return cursor.rowcount > 0

    def find_by_id(self, keeper_id: int) -> Storekeeper | None:
        cursor = self.conn.execute(
            "SELECT id, name, warehouse_id FROM storekeepers WHERE id = ?",
            (keeper_id,)
        )
        row = cursor.fetchone()
        if not row:
            return None
        return Storekeeper(id=row[0], name=row[1], warehouse_id=row[2])

    def find_all(self) -> list[Storekeeper]:
        cursor = self.conn.execute(
            "SELECT id, name, warehouse_id FROM storekeepers ORDER BY name"
        )
        return [Storekeeper(id=r[0], name=r[1], warehouse_id=r[2]) for r in cursor.fetchall()]