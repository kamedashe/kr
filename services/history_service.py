from dao.history_dao import HistoryDAO


class HistoryService:
    """Business logic for supply history."""

    def __init__(self, dao: HistoryDAO):
        self.dao = dao

    def list_all(self) -> list[dict]:
        return self.dao.fetch_records()
