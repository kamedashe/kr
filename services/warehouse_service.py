from dao.warehouse_dao import WarehouseDAO
from models.warehouse import Warehouse

class WarehouseService:
    """CRUD‑логіка для складів"""
    def __init__(self, dao: WarehouseDAO):
        self.dao = dao

    def create(self, warehouse: Warehouse) -> Warehouse:
        warehouse.validate()
        warehouse.id = self.dao.insert(warehouse)
        return warehouse

    def update(self, warehouse: Warehouse) -> bool:
        if warehouse.id is None:
            raise ValueError("Warehouse must have ID before update")
        warehouse.validate()
        return self.dao.update(warehouse)

    def delete(self, wh_id: int) -> bool:
        if not isinstance(wh_id, int):
            raise ValueError("ID must be int")
        return self.dao.delete(wh_id)

    def get_by_id(self, wh_id: int) -> Warehouse | None:
        if not isinstance(wh_id, int):
            raise ValueError("ID must be int")
        return self.dao.find_by_id(wh_id)

    def list_all(self) -> list[Warehouse]:
        return self.dao.find_all()