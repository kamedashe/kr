from typing import List, Dict, Any

class SupplierReportStrategy:
    def fetch_data(self, conn) -> List[Dict[str, Any]]:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT sup.id, sup.name, COUNT(s.id) as total_supplies
            FROM suppliers sup
            LEFT JOIN supplies s ON sup.id = s.supplier_id
            GROUP BY sup.id, sup.name
            ORDER BY total_supplies DESC
        """)
        rows = cursor.fetchall()
        return [
            {"ID": row[0], "Name": row[1], "Total Supplies": row[2]}
            for row in rows
        ]