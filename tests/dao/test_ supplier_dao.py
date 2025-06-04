import sqlite3
import pytest
from models.supplier import Supplier
from dao.supplier_dao import SupplierDAO

@pytest.fixture
def dao():
    conn = sqlite3.connect(':memory:')
    return SupplierDAO(conn)

def test_insert_and_find_by_id(dao):
    s = Supplier(name="Sigma", contact_info="sig@mail.com")
    s_id = dao.insert(s)
    assert s_id > 0
    found = dao.find_by_id(s_id)
    assert found.name == "Sigma"
    assert found.contact_info == "sig@mail.com"

def test_update_and_find_all(dao):
    s = Supplier(name="Beta", contact_info="b@b.com")
    dao.insert(s)
    s.name = "Alpha"
    dao.update(s)
    all_s = dao.find_all()
    assert any(x.name == "Alpha" for x in all_s)

def test_delete(dao):
    s = Supplier(name="ToDelete", contact_info="none")
    dao.insert(s)
    assert dao.delete(s.id)
    assert dao.find_by_id(s.id) is None

def test_find_by_name(dao):
    s1 = Supplier(name="AlphaComp", contact_info="a@a.com")
    s2 = Supplier(name="Betta", contact_info="b@b.com")
    dao.insert(s1)
    dao.insert(s2)
    results = dao.find_by_name("Alpha")
    assert len(results) == 1 and results[0].name == "AlphaComp"
