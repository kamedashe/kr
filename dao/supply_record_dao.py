
import sqlite3
from typing import Optional, Callable
from models.supply_record import SupplyRecord

class SupplyRecordDAO:
    """Data Access Object для таблиці supply_records.

    Параметри
    ----------
    conn : sqlite3.Connection
        Підключення до бази.
    observer : Optional[object]
        Будь‑який об’єкт з методом ``update(record: SupplyRecord)``.
        Якщо передано, буде викликано після успішного ``insert``.
    """

    def __init__(self, conn: sqlite3.Connection, observer: Optional[object] = None):
        self.conn = conn
        self.observer = observer
        self._ensure_table()

    # ---------- Schema ----------
    def _ensure_table(self):
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS supply_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                supply_id INTEGER,
                component_id INTEGER,
                quantity INTEGER,
                price REAL,
                FOREIGN KEY (supply_id) REFERENCES supplies(id),
                FOREIGN KEY (component_id) REFERENCES components(id)
            )
            """
        )
        self.conn.commit()

    # ---------- CRUD ----------
    def insert(self, record: SupplyRecord) -> int:
        with self.conn:
            cur = self.conn.execute(
                """INSERT INTO supply_records
                       (supply_id, component_id, quantity, price)
                       VALUES (?,?,?,?)""",
                (record.supply_id, record.component_id, record.quantity, record.price),
            )
            record.id = cur.lastrowid
        # notify observer
        if self.observer and hasattr(self.observer, "update"):
            try:
                self.observer.update(record)
            except Exception as e:
                print(f"[SupplyRecordDAO] Observer update failed: {e}")
        return record.id

    def find_by_supply(self, supply_id: int) -> list[SupplyRecord]:
        cur = self.conn.execute(
            """SELECT id, supply_id, component_id, quantity, price
                   FROM supply_records
                   WHERE supply_id = ?""",
            (supply_id,),
        )
        rows = cur.fetchall()
        return [
            SupplyRecord(
                id=r[0],
                supply_id=r[1],
                component_id=r[2],
                quantity=r[3],
                price=r[4],
            )
            for r in rows
        ]

    def delete(self, record_id: int) -> bool:
        with self.conn:
            cur = self.conn.execute("DELETE FROM supply_records WHERE id = ?", (record_id,))
        return cur.rowcount > 0
