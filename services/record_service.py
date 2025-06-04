from dao.supply_record_dao import SupplyRecordDAO

class RecordService:
    """Фасад для маніпуляцій із записами поставок."""
    def __init__(self, record_dao: SupplyRecordDAO):
        self.record_dao = record_dao

    def add_record(self, record):
        return self.record_dao.insert(record)

    def delete_record(self, record_id: int):
        return self.record_dao.delete(record_id)

    def get_records_by_supply(self, supply_id: int):
        return self.record_dao.find_by_supply(supply_id)
