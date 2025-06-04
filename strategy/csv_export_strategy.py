import csv
from strategy.export_strategy import ExportStrategy

class CSVExportStrategy(ExportStrategy):
    def export(self, rows, out_path):
        with open(out_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
        return out_path
