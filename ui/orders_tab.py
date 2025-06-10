
from tkinter import ttk


class OrdersTab(ttk.Frame):
    """UI for managing purchase orders."""

    def __init__(self, parent):
        super().__init__(parent)

        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill="x", pady=5)

        ttk.Button(
            btn_frame,
            text="Create order",
            command=lambda: self.ctrl.create_order(),
        ).pack(side="left", padx=5)

        ttk.Button(
            btn_frame,
            text="Check contract",
            command=lambda: self.ctrl.check_contract(),
        ).pack(side="left", padx=5)

        self.table = ttk.Treeview(self, columns=("id", "details"), show="headings")
        self.table.heading("id", text="ID")
        self.table.heading("details", text="Details")
        self.table.pack(fill="both", expand=True)

    def set_controller(self, ctrl):
        self.ctrl = ctrl

    def refresh(self, orders: list[dict]):
        for row in self.table.get_children():
            self.table.delete(row)
        for order in orders:
            self.table.insert("", "end", iid=order["id"], values=(order["id"], order.get("details", "")))
