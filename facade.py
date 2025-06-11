from db.database import get_connection
from dao.supplier_dao import SupplierDAO
from dao.component_dao import ComponentDAO
from dao.supply_dao import SupplyDAO
from dao.warehouse_dao import WarehouseDAO
from dao.order_dao import OrderDAO


class Facade:
    """Aggregate all DAO objects for easy access."""

    def __init__(self, conn=None):
        self.conn = conn or get_connection()
        self.supplier_dao = SupplierDAO(self.conn)
        self.component_dao = ComponentDAO(self.conn)
        self.supply_dao = SupplyDAO(self.conn)
        self.warehouse_dao = WarehouseDAO(self.conn)
        self.order_dao = OrderDAO(self.conn)
