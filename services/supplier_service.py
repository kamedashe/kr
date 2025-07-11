from dao.supplier_dao import SupplierDAO


class SupplierService:
    """Business logic for suppliers using dict DTOs."""

    def __init__(self, dao: SupplierDAO):
        self.dao = dao

    def create(self, dto: dict) -> int:
        return self.dao.insert(dto)

    def update(self, supplier: dict) -> bool:
        return self.dao.update(supplier)

    def delete(self, supplier_id: int) -> bool:
        return self.dao.delete(supplier_id)

    def list_all(self) -> list[dict]:
        return self.dao.select_all()

    def get(self, supplier_id: int) -> dict | None:
        """Return supplier by ID."""
        return self.dao.select_by_id(supplier_id)
