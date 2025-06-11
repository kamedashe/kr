from db.database import get_connection
from dao.warehouse_dao import WarehouseDAO


def test_register_expense():
    conn = get_connection(":memory:")
    dao = WarehouseDAO(conn)
    comp_id = dao.insert({"name": "Bolt", "unit": "pcs", "quantity_in_stock": 5})
    dao.register_expense(comp_id, 2)
    row = dao.select_by_id(comp_id)
    assert row["quantity_in_stock"] == 3
