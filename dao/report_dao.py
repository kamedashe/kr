
class ReportDAO:
    """SQLite DAO for report. Implement CRUD methods"""
    def __init__(self, conn):
        self.conn = conn
