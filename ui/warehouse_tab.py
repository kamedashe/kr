
from tkinter import ttk, IntVar

class WarehouseTab(ttk.Frame):
    """UI for viewing stock levels and registering expenses."""

    def __init__(self, parent):
        super().__init__(parent)
        self.component_id_var = IntVar()
        self.qty_var = IntVar()

        form = ttk.Frame(self)
        form.pack(fill="x", pady=5)
        ttk.Label(form, text="Component ID:").grid(row=0, column=0, padx=5)
        ttk.Entry(form, textvariable=self.component_id_var).grid(row=0, column=1, padx=5)
        ttk.Label(form, text="Qty:").grid(row=0, column=2, padx=5)
        ttk.Entry(form, textvariable=self.qty_var).grid(row=0, column=3, padx=5)

        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill="x", pady=5)

        ttk.Button(
            btn_frame,
            text="Show stock",
            command=lambda: self.ctrl.show_stock(),
        ).pack(side="left", padx=5)

        ttk.Button(
            btn_frame,
            text="Register expense",
            command=lambda: self.ctrl.register_expense(),
        ).pack(side="left", padx=5)

        self.table = ttk.Treeview(self, columns=("component", "qty"), show="headings")
        self.table.heading("component", text="Component")
        self.table.heading("qty", text="Quantity")
        self.table.pack(fill="both", expand=True)

    def set_controller(self, ctrl):
        self.ctrl = ctrl

    def refresh(self, data: list[dict]):
        for row in self.table.get_children():
            self.table.delete(row)
        for item in data:
            self.table.insert(
                "",
                "end",
                iid=item["id"],
                values=(item["name"], item.get("quantity_in_stock", 0)),
            )
