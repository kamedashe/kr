
class Supply_recordDAO:
    """SQLite DAO for supply_record. Implement CRUD methods"""
    def __init__(self, conn):
        self.conn = conn
