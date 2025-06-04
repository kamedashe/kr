from strategy.export_strategy import ExportStrategy

class ReportService:
    def __init__(self):
        self.strategy: ExportStrategy = None

    def set_strategy(self, strategy: ExportStrategy):
        self.strategy = strategy

    def export(self, rows, out_path):
        if not self.strategy:
            raise Exception("Стратегія експорту не вибрана!")
        return self.strategy.export(rows, out_path)
