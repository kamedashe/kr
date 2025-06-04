from typing import List, Dict, Any

class SupplyReportStrategy:
    def fetch_data(self, conn) -> List[Dict[str, Any]]:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT s.id, s.date, sup.name AS supplier, w.name AS warehouse
            FROM supplies s
            JOIN suppliers sup ON s.supplier_id = sup.id
            JOIN warehouses w ON s.warehouse_id = w.id
            ORDER BY s.date DESC
        """)
        rows = cursor.fetchall()
        return [
            {"ID": row[0], "Date": row[1], "Supplier": row[2], "Warehouse": row[3]}
            for row in rows
        ]