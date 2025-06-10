import pytest
from db.database import get_connection
from dao.supplier_dao import SupplierDAO
from services.supplier_service import SupplierService

@pytest.fixture
def service():
    conn = get_connection(":memory:")
    dao = SupplierDAO(conn)
    return SupplierService(dao)

@pytest.fixture
def sample_supplier(service):
    dto = {"name": "Bolt", "contact_info": ""}
    dto["id"] = service.create(dto)
    return dto

def test_create_supplier(service):
    dto = {"name": "ACME", "contact_info": "info@acme"}
    supplier_id = service.create(dto)
    suppliers = service.list_all()
    assert supplier_id == suppliers[0]["id"]
    assert suppliers[0]["name"] == "ACME"

def test_update(service, sample_supplier):
    dto = {"id": sample_supplier["id"], "name": "Bolt", "contact_info": ""}
    assert service.update(dto) is True
    updated = service.list_all()[0]
    assert updated["name"] == "Bolt"
