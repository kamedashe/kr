import sqlite3
import pytest
from models.storekeeper import Storekeeper
from dao.storekeeper_dao import StorekeeperDAO
from dao.warehouse_dao import WarehouseDAO
from models.warehouse import Warehouse

@pytest.fixture
def dao():
    conn = sqlite3.connect(':memory:')
    # Створюємо таблицю warehouses, бо foreign key
    WarehouseDAO(conn).insert(Warehouse(name="W1", location="X"))
    return StorekeeperDAO(conn)

def test_insert_and_find_by_id(dao):
    k = Storekeeper(name="Ivan", warehouse_id=1)
    k_id = dao.insert(k)
    assert k_id > 0
    found = dao.find_by_id(k_id)
    assert found.name == "Ivan"
    assert found.warehouse_id == 1

def test_update_and_find_all(dao):
    k = Storekeeper(name="Ivan", warehouse_id=1)
    dao.insert(k)
    k.name = "Stepan"
    dao.update(k)
    all_k = dao.find_all()
    assert any(x.name == "Stepan" for x in all_k)

def test_delete(dao):
    k = Storekeeper(name="Petro", warehouse_id=1)
    dao.insert(k)
    assert dao.delete(k.id)
    assert dao.find_by_id(k.id) is None
