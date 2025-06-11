import pytest
from db.database import get_connection
from dao.warehouse_dao import WarehouseDAO

@pytest.fixture
def dao():
    conn = get_connection(':memory:')
    return WarehouseDAO(conn)

def test_register_expense_success(dao):
    comp_id = dao.insert({'name': 'Bolt', 'unit': 'pcs', 'quantity_in_stock': 5})
    dao.register_expense(comp_id, 3)
    row = dao.select_by_id(comp_id)
    assert row['quantity_in_stock'] == 2

def test_register_expense_insufficient_stock(dao):
    comp_id = dao.insert({'name': 'Nut', 'unit': 'pcs', 'quantity_in_stock': 1})
    with pytest.raises(ValueError):
        dao.register_expense(comp_id, 2)
