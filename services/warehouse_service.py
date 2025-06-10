from services.component_service import ComponentService
from dao.warehouse_dao import WarehouseDAO


class WarehouseService(ComponentService):
    """Service wrapper for warehouse operations."""

    def __init__(self, dao: WarehouseDAO):
        super().__init__(dao)
