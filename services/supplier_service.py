from dao.supplier_dao import SupplierDAO
from models.supplier import Supplier

class SupplierService:
    def __init__(self, dao: SupplierDAO):
        self.dao = dao

    def create(self, supplier: Supplier) -> Supplier:
        supplier.validate()
        supplier.id = self.dao.insert(supplier)
        return supplier

    def update(self, supplier: Supplier) -> bool:
        if supplier.id is None:
            raise ValueError("Supplier must have an ID to be updated.")
        supplier.validate()
        return self.dao.update(supplier)

    def delete(self, supplier_id: int) -> bool:
        if not isinstance(supplier_id, int):
            raise ValueError("Supplier ID must be an integer.")
        return self.dao.delete(supplier_id)

    def get_by_id(self, supplier_id: int) -> Supplier | None:
        if not isinstance(supplier_id, int):
            raise ValueError("Supplier ID must be an integer.")
        return self.dao.find_by_id(supplier_id)

    def list_all(self) -> list[Supplier]:
        return self.dao.find_all()
