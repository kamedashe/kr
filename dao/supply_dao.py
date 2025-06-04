import sqlite3
from datetime import datetime
from models.supply import Supply

class SupplyDAO:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.create_table()

    def create_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS supplies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                supplier_id INTEGER,
                warehouse_id INTEGER,
                storekeeper_id INTEGER,
                FOREIGN KEY (supplier_id) REFERENCES suppliers(id),
                FOREIGN KEY (warehouse_id) REFERENCES warehouses(id),
                FOREIGN KEY (storekeeper_id) REFERENCES storekeepers(id)
            )
        """)
        self.conn.commit()

    def insert(self, supply: Supply) -> int:
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO supplies (date, supplier_id, warehouse_id, storekeeper_id)
            VALUES (?, ?, ?, ?)
        """, (supply.supply_date.isoformat(), supply.supplier_id, supply.warehouse_id, supply.storekeeper_id))
        self.conn.commit()
        supply.id = cursor.lastrowid
        return supply.id

    def find_all(self) -> list[Supply]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM supplies")
        rows = cursor.fetchall()
        return [
            Supply(
                id=row[0],
                supply_date=datetime.fromisoformat(row[1]).date(),
                supplier_id=row[2],
                warehouse_id=row[3],
                storekeeper_id=row[4]
            ) for row in rows
        ]
