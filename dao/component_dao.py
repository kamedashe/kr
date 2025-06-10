import sqlite3


class ComponentDAO:
    """SQLite DAO for components using dict-based DTOs."""

    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self._create_table()

    def _create_table(self) -> None:
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS components (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                unit TEXT NOT NULL,
                quantity_in_stock INTEGER NOT NULL DEFAULT 0
            )
            """
        )
        self.conn.commit()

    def insert(self, component: dict) -> int:
        """Insert component and return its new ID."""
        with self.conn:
            cur = self.conn.execute(
                "INSERT INTO components (name, unit, quantity_in_stock) VALUES (?, ?, ?)",
                (
                    component.get("name"),
                    component.get("unit"),
                    component.get("quantity_in_stock", 0),
                ),
            )
        return cur.lastrowid

    def update(self, component: dict) -> bool:
        """Update component by ID using dict fields."""
        with self.conn:
            cur = self.conn.execute(
                """UPDATE components
                       SET name = ?, unit = ?, quantity_in_stock = ?
                     WHERE id = ?""",
                (
                    component.get("name"),
                    component.get("unit"),
                    component.get("quantity_in_stock", 0),
                    component.get("id"),
                ),
            )
        return cur.rowcount > 0

    def delete(self, component_id: int) -> bool:
        """Delete component by ID."""
        with self.conn:
            cur = self.conn.execute(
                "DELETE FROM components WHERE id = ?",
                (component_id,),
            )
        return cur.rowcount > 0

    def select_by_id(self, component_id: int) -> dict | None:
        cur = self.conn.execute(
            "SELECT id, name, unit, quantity_in_stock FROM components WHERE id = ?",
            (component_id,),
        )
        row = cur.fetchone()
        if row:
            return {
                "id": row[0],
                "name": row[1],
                "unit": row[2],
                "quantity_in_stock": row[3],
            }
        return None

    def select_all(self) -> list[dict]:
        cur = self.conn.execute(
            "SELECT id, name, unit, quantity_in_stock FROM components ORDER BY name"
        )
        return [
            {
                "id": r[0],
                "name": r[1],
                "unit": r[2],
                "quantity_in_stock": r[3],
            }
            for r in cur.fetchall()
        ]

    def select_by_name(self, name_substring: str) -> list[dict]:
        pattern = f"%{name_substring}%"
        cur = self.conn.execute(
            """SELECT id, name, unit, quantity_in_stock
               FROM components WHERE name LIKE ? ORDER BY name""",
            (pattern,),
        )
        return [
            {
                "id": r[0],
                "name": r[1],
                "unit": r[2],
                "quantity_in_stock": r[3],
            }
            for r in cur.fetchall()
        ]

    def update_quantity(self, component_id: int, delta: int) -> None:
        with self.conn:
            self.conn.execute(
                "UPDATE components SET quantity_in_stock = quantity_in_stock + ? WHERE id = ?",
                (delta, component_id),
            )
