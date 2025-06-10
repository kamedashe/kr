import pytest
from db.database import get_connection
from dao.component_dao import ComponentDAO

@pytest.fixture
def dao():
    conn = get_connection(":memory:")
    return ComponentDAO(conn)

def test_insert_and_select(dao):
    comp_id = dao.insert({"name": "Bolt", "unit": "pcs", "quantity_in_stock": 10})
    row = dao.select_by_id(comp_id)
    assert row["name"] == "Bolt"
    assert row["quantity_in_stock"] == 10

def test_update_quantity(dao):
    comp_id = dao.insert({"name": "Nut", "unit": "pcs", "quantity_in_stock": 5})
    dao.update_quantity(comp_id, 3)
    row = dao.select_by_id(comp_id)
    assert row["quantity_in_stock"] == 8
