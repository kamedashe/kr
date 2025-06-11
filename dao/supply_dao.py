import sqlite3


class SupplyDAO:
    """SQLite DAO for supply history retrieval."""

    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def get_history_by_supplier(self, supplier_id: int) -> list[tuple[str, str, int]]:
        """Return supply history rows for the given supplier."""
        cur = self.conn.execute(
            """
            SELECT sh.date, c.name, sh.qty
              FROM supply_history sh
              JOIN components c ON c.id = sh.component_id
             WHERE sh.supplier_id = ?
             ORDER BY sh.date DESC
            """,
            (supplier_id,),
        )
        return [(row[0], row[1], row[2]) for row in cur.fetchall()]
