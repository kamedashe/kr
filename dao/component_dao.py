import sqlite3
from models.component import Component

class ComponentDAO:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.create_table()
        self.ensure_column()

    def create_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS components (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                unit TEXT NOT NULL,
                quantity_in_stock INTEGER NOT NULL DEFAULT 0
            )
        """)
        self.conn.commit()

    def ensure_column(self):
        cursor = self.conn.execute("PRAGMA table_info(components)")
        cols = [row[1] for row in cursor.fetchall()]
        if "quantity_in_stock" not in cols:
            self.conn.execute(
                "ALTER TABLE components ADD COLUMN quantity_in_stock INTEGER NOT NULL DEFAULT 0"
            )
            self.conn.commit()

    def insert(self, component: Component) -> int:
        with self.conn:
            cursor = self.conn.execute(
                "INSERT INTO components (name, unit, quantity_in_stock) VALUES (?, ?, ?)",
                (component.name, component.unit, component.quantity_in_stock)
            )
        component.id = cursor.lastrowid
        return component.id

    def update(self, component: Component) -> bool:
        with self.conn:
            cursor = self.conn.execute(
                "UPDATE components SET name = ?, unit = ? WHERE id = ?",
                (component.name, component.unit, component.id)
            )
        return cursor.rowcount > 0

    def delete(self, component_id: int) -> bool:
        with self.conn:
            cursor = self.conn.execute(
                "DELETE FROM components WHERE id = ?",
                (component_id,)
            )
        return cursor.rowcount > 0

    def update_quantity(self, component_id: int, delta: int) -> None:
        with self.conn:
            self.conn.execute(
                "UPDATE components SET quantity_in_stock = quantity_in_stock + ? WHERE id = ?",
                (delta, component_id)
            )

    def find_by_id(self, component_id: int) -> Component | None:
        cursor = self.conn.execute(
            "SELECT id, name, unit, quantity_in_stock FROM components WHERE id = ?",
            (component_id,)
        )
        row = cursor.fetchone()
        if not row:
            return None
        return Component(id=row[0], name=row[1], unit=row[2], quantity_in_stock=row[3])

    def find_all(self) -> list[Component]:
        cursor = self.conn.execute(
            "SELECT id, name, unit, quantity_in_stock FROM components ORDER BY name"
        )
        return [
            Component(id=r[0], name=r[1], unit=r[2], quantity_in_stock=r[3])
            for r in cursor.fetchall()
        ]
