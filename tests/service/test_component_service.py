import pytest
from unittest.mock import MagicMock
from services.component_service import ComponentService
from models.component import Component

@pytest.fixture
def dao():
    mock = MagicMock()
    return mock

@pytest.fixture
def service(dao):
    return ComponentService(dao)

def test_increment_stock_valid(service, dao):
    dao.update_quantity.return_value = None
    service.increment_stock(5, 3)
    dao.update_quantity.assert_called_once_with(5, 3)

def test_increment_stock_invalid_id(service):
    with pytest.raises(ValueError):
        service.increment_stock("bad", 2)

def test_increment_stock_invalid_delta(service):
    with pytest.raises(ValueError):
        service.increment_stock(5, "not int")
