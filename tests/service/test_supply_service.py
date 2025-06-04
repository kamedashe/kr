import pytest
from unittest.mock import MagicMock
from services.supply_service import SupplyService
from models.supply import Supply
from models.supply_record import SupplyRecord
from datetime import date

@pytest.fixture
def supply_dao():
    return MagicMock()

@pytest.fixture
def record_dao():
    return MagicMock()

@pytest.fixture
def service(supply_dao, record_dao):
    return SupplyService(supply_dao, record_dao)

def test_register_supply_ok(service, supply_dao, record_dao):
    supply = Supply(
        supply_date=date(2024, 5, 30),
        supplier_id=1,
        warehouse_id=1,
        storekeeper_id=1
    )
    records = [
        SupplyRecord(supply_id=None, component_id=1, quantity=10, price=100.0),
        SupplyRecord(supply_id=None, component_id=2, quantity=5, price=50.0)
    ]
    supply_dao.insert.side_effect = lambda s: setattr(s, 'id', 1) or 1
    service.register_supply(supply, records)
    supply_dao.insert.assert_called_once_with(supply)
    assert all(r.supply_id == 1 for r in records)
    assert record_dao.insert.call_count == 2

def test_register_supply_empty_records(service):
    supply = Supply(
        supply_date=date(2024, 5, 30),
        supplier_id=1,
        warehouse_id=1,
        storekeeper_id=1
    )
    with pytest.raises(ValueError):
        service.register_supply(supply, [])
