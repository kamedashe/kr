from services.record_service import RecordService
from dao.supply_record_dao import SupplyRecordDAO

class MockSupplyRecordDAO(SupplyRecordDAO):
    def __init__(self):
        pass
    def insert(self, record):
        return 123
    def delete(self, record_id):
        return True
    def find_by_supply(self, supply_id):
        return ["recX"]

def test_add_record():
    dao = MockSupplyRecordDAO()
    service = RecordService(dao)
    assert service.add_record({"fake": "record"}) == 123

def test_delete_record():
    dao = MockSupplyRecordDAO()
    service = RecordService(dao)
    assert service.delete_record(7) is True

def test_get_records_by_supply():
    dao = MockSupplyRecordDAO()
    service = RecordService(dao)
    assert service.get_records_by_supply(42) == ["recX"]
