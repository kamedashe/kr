from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename


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
        rows = self.history_service.list_all()
        if not rows:
            messagebox.showinfo("Report", "No supply history available")
            return
        path = asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV", "*.csv"), ("PDF", "*.pdf")],
        )
        if path:
            kind = "pdf" if path.endswith(".pdf") else "csv"
            self.report_service.export(kind, rows, path)

    def show_supply_history(self):
        """Refresh the view with supply history."""
        self.view.refresh(self.history_service.list_all())
