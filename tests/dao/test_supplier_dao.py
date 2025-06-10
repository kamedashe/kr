import pytest
from db.database import get_connection
from dao.supplier_dao import SupplierDAO

@pytest.fixture
def dao():
    conn = get_connection(":memory:")
    return SupplierDAO(conn)


def test_insert_and_select(dao):
    supplier_id = dao.insert({"name": "ACME", "contact_info": "info"})
    row = dao.select_by_id(supplier_id)
    assert row["name"] == "ACME"


def test_update_by_id(dao):
    supplier_id = dao.insert({"name": "Old", "contact_info": ""})
    dao.update(supplier_id, {"name": "New", "contact_info": ""})
    row = dao.select_by_id(supplier_id)
    assert row["name"] == "New"


def test_delete_with_dict(dao):
    supplier_id = dao.insert({"name": "Temp", "contact_info": ""})
    assert dao.delete({"id": supplier_id}) is True
    assert dao.select_by_id(supplier_id) is None
