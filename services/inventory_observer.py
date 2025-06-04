
from dao.component_dao import ComponentDAO
from models.supply_record import SupplyRecord

class InventoryObserver:
    """Оновлює залишки компонентів після додавання запису поставки."""

    def __init__(self, component_dao: ComponentDAO):
        self.component_dao = component_dao

    def update(self, record: SupplyRecord):
        # Додаємо кількість до складу
        self.component_dao.update_quantity(record.component_id, record.quantity)
        print(f"[Observer] Залишки оновлено: +{record.quantity} для компоненту {record.component_id}")
