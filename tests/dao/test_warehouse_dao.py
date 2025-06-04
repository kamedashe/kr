import sqlite3
import pytest
from models.warehouse import Warehouse
from dao.warehouse_dao import WarehouseDAO

@pytest.fixture
def dao():
    conn = sqlite3.connect(':memory:')
    return WarehouseDAO(conn)

def test_insert_and_find_by_id(dao):
    w = Warehouse(name="Main", location="Kyiv")
    w_id = dao.insert(w)
    assert w_id > 0
    result = dao.find_by_id(w_id)
    assert result.name == "Main"
    assert result.location == "Kyiv"

def test_update_and_find_all(dao):
    w = Warehouse(name="Main", location="Kyiv")
    dao.insert(w)
    w.name = "Updated"
    dao.update(w)
    all_ws = dao.find_all()
    assert any(x.name == "Updated" for x in all_ws)

def test_delete(dao):
    w = Warehouse(name="Delete", location="Lviv")
    dao.insert(w)
    ok = dao.delete(w.id)
    assert ok
    assert dao.find_by_id(w.id) is None
