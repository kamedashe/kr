from dao.component_dao import ComponentDAO


class WarehouseDAO(ComponentDAO):
    """Alias DAO for warehouse operations using components table."""

    def __init__(self, conn):
        super().__init__(conn)

    def register_expense(self, component_id: int, qty: int) -> None:
        """Decrease stock for ``component_id`` by ``qty``."""
        self.update_quantity(component_id, -abs(qty))
