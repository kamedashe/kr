from controllers.supplier_controller import SupplierController


class SuppliersController(SupplierController):
    """Alias controller matching naming convention."""

    def list_all_suppliers(self) -> list[tuple[int, str, str]]:
        """Return all suppliers ordered by ``id`` ascending."""
        return self.facade.supplier_dao.get_all()
