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
