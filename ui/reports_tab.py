
from tkinter import ttk


class ReportsTab(ttk.Frame):
    """UI tab for reports and supply history preview."""

    def __init__(self, parent):
        super().__init__(parent)
        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill="x", pady=5)

        ttk.Button(
            btn_frame,
            text="Generate report",
            command=lambda: self.ctrl.generate_report(),
        ).pack(side="left", padx=5)

        ttk.Button(
            btn_frame,
            text="Supply history",
            command=lambda: self.ctrl.show_supply_history(),
        ).pack(side="left", padx=5)

        self.table = ttk.Treeview(
            self,
            columns=("id", "supplier", "component", "qty", "date"),
            show="headings",
        )
        self.table.heading("id", text="ID")
        self.table.heading("supplier", text="Supplier")
        self.table.heading("component", text="Component")
        self.table.heading("qty", text="Qty")
        self.table.heading("date", text="Date")
        self.table.pack(fill="both", expand=True)

    def set_controller(self, ctrl):
        self.ctrl = ctrl

    def refresh(self, rows: list[dict]):
        for row in self.table.get_children():
            self.table.delete(row)
        for r in rows:
            self.table.insert(
                "",
                "end",
                iid=r.get("id"),
                values=(r.get("id"), r.get("supplier"), r.get("component"), r.get("qty"), r.get("date")),
            )
