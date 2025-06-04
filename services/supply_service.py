from dao.supply_dao import SupplyDAO
from dao.supply_record_dao import SupplyRecordDAO
from models.supply import Supply
from models.supply_record import SupplyRecord

class SupplyService:
    """Реєстрація поставок + Observer (оновлення складу)."""
    def __init__(self, supply_dao: SupplyDAO, record_dao: SupplyRecordDAO):
        self.supply_dao = supply_dao
        self.record_dao = record_dao

    def register_supply(self, supply: Supply, records: list[SupplyRecord]) -> Supply:
        if not records:
            raise ValueError("Supply must contain at least one record")
        # 1. Вставка поставки
        self.supply_dao.insert(supply)  # заповнює supply.id
        # 2. Вставка позицій
        for rec in records:
            rec.supply_id = supply.id
            self.record_dao.insert(rec)  # Observer збільшить залишки
        return supply