from db.database import get_connection
from dao.warehouse_dao import WarehouseDAO
from services.warehouse_service import WarehouseService


def create_service():
    conn = get_connection(":memory:")
    dao = WarehouseDAO(conn)
    return WarehouseService(dao)


def test_register_expense():
    service = create_service()
    comp_id = service.create({"name": "Bolt", "unit": "pcs", "quantity_in_stock": 5})
    service.register_expense(comp_id, 2)
    row = service.get(comp_id)
    assert row["quantity_in_stock"] == 3
