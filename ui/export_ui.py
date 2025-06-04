from tkinter import Button, messagebox, ttk
from tkinter.filedialog import asksaveasfilename
from services.report_service import ReportService
from strategy.csv_export_strategy import CSVExportStrategy
from strategy.pdf_export_strategy import PDFExportStrategy
from strategy.supplier_report_strategy import SupplierReportStrategy
from strategy.supply_report_strategy import SupplyReportStrategy
from db.database import get_connection

def create_export_ui(root):
    conn = get_connection()
    report_service = ReportService()

    report_cb = ttk.Combobox(root, state="readonly", values=[
        "Постачальники (Supplier Report)",
        "Поставки (Supply Report)"
    ])
    report_cb.pack(pady=5)

    def export(kind):
        report_type = report_cb.get()
        if "Supplier" in report_type:
            rows = SupplierReportStrategy().fetch_data(conn)
        elif "Supply" in report_type:
            rows = SupplyReportStrategy().fetch_data(conn)
        else:
            messagebox.showwarning("Помилка", "Оберіть тип звіту")
            return

        path = asksaveasfilename(defaultextension=f".{kind}", filetypes=[("CSV", "*.csv")] if kind == 'csv' else [("PDF", "*.pdf")])
        if not path:
            return

        if kind == 'csv':
            report_service.set_strategy(CSVExportStrategy())
        else:
            report_service.set_strategy(PDFExportStrategy())

        try:
            report_service.export(rows, path)
            messagebox.showinfo("Експорт", f"Файл збережено: {path}")
        except Exception as e:
            messagebox.showerror("Помилка", str(e))

    btn_csv = Button(root, text="Export CSV", command=lambda: export('csv'))
    btn_pdf = Button(root, text="Export PDF", command=lambda: export('pdf'))

    btn_csv.pack()
    btn_pdf.pack()

    return report_cb, btn_csv, btn_pdf
