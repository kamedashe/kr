from dao.component_dao import ComponentDAO


class WarehouseDAO(ComponentDAO):
    """Alias DAO for warehouse operations using components table."""

    def __init__(self, conn):
        super().__init__(conn)

    def register_expense(self, component_id: int, qty: int) -> None:
        """Register usage of a component and log it into supply history."""
        with self.conn as con:
            cur = con.execute(
                "SELECT quantity_in_stock FROM components WHERE id = ?",
                (component_id,),
            )
            row = cur.fetchone()
            if row is None:
                raise ValueError("Component not found")
            current_qty = row[0]
            if qty > current_qty:
                raise ValueError("Insufficient stock")

            con.execute(
                "UPDATE components SET quantity_in_stock = quantity_in_stock - ? WHERE id = ?",
                (qty, component_id),
            )

            con.execute(
                "INSERT INTO supply_history(component_id, qty, date) VALUES (?, ?, CURRENT_TIMESTAMP)",
                (component_id, qty),
            )
