from services.receipt_service import ReceiptService

class MockSupplyDAO:
    def find_by_id(self, id):
        return {"id": id}

class MockSupplyRecordDAO:
    def find_by_supply(self, supply_id):
        return [{"rec": 1}]

def test_get_receipt_returns_data():
    supply_dao = MockSupplyDAO()
    record_dao = MockSupplyRecordDAO()
    service = ReceiptService(supply_dao, record_dao)
    receipt = service.get_receipt(5)
    assert receipt["supply"] == {"id": 5}
    assert receipt["records"] == [{"rec": 1}]
