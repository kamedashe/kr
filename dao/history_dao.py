import sqlite3


class HistoryDAO:
    """DAO for supply history records."""

    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self._ensure_table()

    def _ensure_table(self) -> None:
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS supply_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT
            )
            """
        )
        self.conn.commit()

    def fetch_records(self) -> list[dict]:
        cur = self.conn.execute("SELECT id, description FROM supply_history ORDER BY id")
        return [{"id": r[0], "description": r[1]} for r in cur.fetchall()]
