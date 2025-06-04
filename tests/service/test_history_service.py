from services.history_service import HistoryService
from dao.history_dao import HistoryDAO

class MockHistoryDAO(HistoryDAO):
    def fetch_records(self, filters=None):
        return ["rec1", "rec2"]

def test_get_history_returns_records():
    dao = MockHistoryDAO()
    service = HistoryService(dao)
    result = service.get_history()
    assert result == ["rec1", "rec2"]
