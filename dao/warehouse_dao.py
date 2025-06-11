from dao.component_dao import ComponentDAO


class WarehouseDAO(ComponentDAO):
    """Alias DAO for warehouse operations using components table."""

    def __init__(self, conn):
        super().__init__(conn)

    def get_all_stock(self) -> list[tuple[int, str, int]]:
        """Return all components with their current stock quantity."""
        cur = self.conn.execute(
            "SELECT id, name, quantity_in_stock FROM components ORDER BY name"
        )
        return [(r[0], r[1], r[2]) for r in cur.fetchall()]

    def register_expense(self, component_id: int, qty: int) -> None:
        """Decrease stock for the given component by ``qty``.

        Raises ``ValueError`` if the component does not exist or there is
        insufficient stock available.
        """
        cur = self.conn.execute(
            "SELECT quantity_in_stock FROM components WHERE id = ?",
            (component_id,),
        )
        row = cur.fetchone()
        if row is None:
            raise ValueError("Component not found")
        if row[0] < qty:
            raise ValueError("Insufficient stock")

        with self.conn:
            self.conn.execute(
                "UPDATE components SET quantity_in_stock = quantity_in_stock - ? WHERE id = ?",
                (qty, component_id),
            )
