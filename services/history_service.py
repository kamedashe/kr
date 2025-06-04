from dao.supply_dao import SupplyDAO

class HistoryService:
    def __init__(self, history_dao):
        self.history_dao = history_dao

    def get_history(self):
        return self.history_dao.fetch_records()

