class OrderDAO:
    """SQLite DAO for purchase orders."""

    def __init__(self, conn):
        self.conn = conn
        self._create_table()

    def _create_table(self) -> None:
        """Create table for orders if it doesn't exist."""
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                supplier_id INTEGER NOT NULL,
                component_id INTEGER NOT NULL,
                qty INTEGER NOT NULL,
                FOREIGN KEY (supplier_id) REFERENCES suppliers(id),
                FOREIGN KEY (component_id) REFERENCES components(id)
            )
            """
        )
        self.conn.commit()

    def insert(self, order: dict) -> int:
        """Insert order and return new ID."""
        with self.conn:
            cur = self.conn.execute(
                "INSERT INTO orders (supplier_id, component_id, qty) VALUES (?, ?, ?)",
                (
                    order.get("supplier_id"),
                    order.get("component_id"),
                    order.get("qty"),
                ),
            )
        return cur.lastrowid

    def select_all(self) -> list[dict]:
        """Return all orders ordered by id."""
        cur = self.conn.execute(
            "SELECT id, supplier_id, component_id, qty FROM orders ORDER BY id"
        )
        return [
            {
                "id": r[0],
                "supplier_id": r[1],
                "component_id": r[2],
                "qty": r[3],
            }
            for r in cur.fetchall()
        ]

    def get(self, order_id: int):
        """Return single order joined with names for display."""
        cur = self.conn.execute(
            """
            SELECT o.id,
                   s.name AS supplier,
                   c.name || ' x ' || o.qty AS details
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
            "details": row[2],
        }
