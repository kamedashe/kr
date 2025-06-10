from dao.supplier_dao import SupplierDAO


class SupplierService:
    """Business logic for suppliers using dict DTOs."""

    def __init__(self, dao: SupplierDAO):
        self.dao = dao

    def create(self, dto: dict) -> int:
        return self.dao.insert(dto)

    def update(self, dto: dict) -> bool:
        return self.dao.update(dto)

    def delete(self, supplier_id: int) -> bool:
        return self.dao.delete(supplier_id)

    def list_all(self) -> list[dict]:
        return self.dao.select_all()
