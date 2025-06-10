class ReportController:
    """Controller for reports and history."""

    def __init__(self, view=None, report_service=None, history_service=None):
        self.view = view
        self.report_service = report_service
        self.history_service = history_service
        if self.view is not None:
            self.view.set_controller(self)

    def generate_report(self):
        """Generate report using supply history."""
        records = self.history_service.list_all()
        if self.report_service is not None:
            self.report_service.generate(records)

    def show_supply_history(self):
        """Refresh the view with supply history."""
        if self.view is not None:
            self.view.refresh(self.history_service.list_all())
