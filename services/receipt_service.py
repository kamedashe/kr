from dao.supply_dao import SupplyDAO
from dao.supply_record_dao import SupplyRecordDAO

class ReceiptService:
    """Фасад для отримання детальних чеків по поставках."""
    def __init__(self, supply_dao: SupplyDAO, record_dao: SupplyRecordDAO):
        self.supply_dao = supply_dao
        self.record_dao = record_dao

    def get_receipt(self, supply_id: int):
        """Повертає об'єкт поставки та всі записи по цій поставці."""
        supply = self.supply_dao.find_by_id(supply_id)
        records = self.record_dao.find_by_supply(supply_id)
        return {"supply": supply, "records": records}
