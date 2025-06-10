from db.database import get_connection
from dao.component_dao import ComponentDAO
from services.component_service import ComponentService


def create_service():
    conn = get_connection(":memory:")
    dao = ComponentDAO(conn)
    return ComponentService(dao)


def test_create_and_get():
    service = create_service()
    comp_id = service.create({"name": "Bolt", "unit": "pcs", "quantity_in_stock": 5})
    row = service.get(comp_id)
    assert row["name"] == "Bolt"
    assert row["quantity_in_stock"] == 5


def test_adjust_stock():
    service = create_service()
    comp_id = service.create({"name": "Nut", "unit": "pcs", "quantity_in_stock": 2})
    service.adjust_stock(comp_id, 3)
    row = service.get(comp_id)
    assert row["quantity_in_stock"] == 5

