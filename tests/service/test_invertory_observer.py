from unittest.mock import MagicMock
from services.inventory_observer import InventoryObserver
from models.supply_record import SupplyRecord

def test_update_calls_update_quantity():
    dao = MagicMock()
    obs = InventoryObserver(dao)
    record = SupplyRecord(supply_id=1, component_id=2, quantity=5, price=99.99)
    obs.update(record)
    dao.update_quantity.assert_called_once_with(2, 5)
