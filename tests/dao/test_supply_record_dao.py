import sqlite3
import pytest
from models.supply_record import SupplyRecord
from dao.supply_record_dao import SupplyRecordDAO
from dao.supply_dao import SupplyDAO
from dao.component_dao import ComponentDAO
from dao.supplier_dao import SupplierDAO
from dao.warehouse_dao import WarehouseDAO
from dao.storekeeper_dao import StorekeeperDAO
from models.supply import Supply
from models.component import Component
from models.supplier import Supplier
from models.warehouse import Warehouse
from models.storekeeper import Storekeeper
from datetime import date

@pytest.fixture
def dao():
    conn = sqlite3.connect(':memory:')
    # Створюємо всі потрібні таблиці й записи для FK
    SupplierDAO(conn).insert(Supplier(name="S1", contact_info="s1"))
    WarehouseDAO(conn).insert(Warehouse(name="W1", location="Lviv"))
    StorekeeperDAO(conn).insert(Storekeeper(name="K1", warehouse_id=1))
    ComponentDAO(conn).insert(Component(name="Comp1", unit="pcs", quantity_in_stock=100))
    SupplyDAO(conn).insert(Supply(supply_date=date(2025, 5, 30), supplier_id=1, warehouse_id=1, storekeeper_id=1))
    return SupplyRecordDAO(conn)

def test_insert_and_find_by_supply(dao):
    rec = SupplyRecord(supply_id=1, component_id=1, quantity=42, price=3.14)
    rec_id = dao.insert(rec)
    assert rec_id > 0
    found = dao.find_by_supply(1)
    assert any(r.id == rec_id and r.quantity == 42 for r in found)

def test_delete(dao):
    rec = SupplyRecord(supply_id=1, component_id=1, quantity=1, price=1)
    dao.insert(rec)
    assert dao.delete(rec.id)
