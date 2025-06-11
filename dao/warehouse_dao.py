from dao.component_dao import ComponentDAO


class WarehouseDAO(ComponentDAO):
    """Alias DAO for warehouse operations using components table."""

    def __init__(self, conn):
        super().__init__(conn)
        self._ensure_history_table()

    def _ensure_history_table(self) -> None:
        """Create the ``supply_history`` table if needed."""
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS supply_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                supplier_id INTEGER,
                component_id INTEGER NOT NULL,
                qty INTEGER NOT NULL,
                date TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (supplier_id) REFERENCES suppliers(id),
                FOREIGN KEY (component_id) REFERENCES components(id)
            )
            """
        )
        self.conn.commit()

    def get_all_stock(self) -> list[tuple[int, str, int]]:
        """Return all component stock as tuples ordered by ``id``."""
        cur = self.conn.execute(
            "SELECT c.id, c.name, c.quantity_in_stock FROM components c ORDER BY c.id"
        )
        return [(row[0], row[1], row[2]) for row in cur.fetchall()]

    def register_expense(self, component_id: int, qty: int) -> None:
        """Decrease stock for the given component by ``qty``.

        Raises ``ValueError`` if the component does not exist or there is
        insufficient stock available.
        """
        cur = self.conn.execute(
            "SELECT quantity_in_stock FROM components WHERE id=?",
            (component_id,),
        )
        row = cur.fetchone()
        if row is None:
            raise ValueError("Component not found")
        stock = row[0]
        if qty > stock:
            raise ValueError("Insufficient stock")

        with self.conn:
            self.conn.execute(
                "UPDATE components SET quantity_in_stock = quantity_in_stock - ? WHERE id=?",
                (qty, component_id),
            )
            self.conn.execute(
                "INSERT INTO supply_history(supplier_id, component_id, qty, date) VALUES (NULL, ?, ?, CURRENT_TIMESTAMP)",
                (component_id, -qty),
            )
