
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
            command=self._on_check_contract,
        ).pack(side="left", padx=5)

        columns = ("id", "supplier", "component", "qty", "date")
        self.table = ttk.Treeview(self, columns=columns, show="headings")
        for col in columns:
            self.table.heading(col, text=col)
            self.table.column(col, anchor="center")
        self.table.pack(fill="both", expand=True)

        self.populate_orders()

    def set_controller(self, ctrl):
        self.ctrl = ctrl
        # Alias used by populate_orders for consistency with other tabs
        self.controller = ctrl

    def refresh(self, orders: list[dict]):
        for row in self.table.get_children():
            self.table.delete(row)
        for order in orders:
            self.table.insert(
                "",
                "end",
                iid=order[0],
                values=(order[0], order[1], order[2], order[3], order[4]),
            )

    def populate_orders(self) -> None:
        """Populate the orders table using the attached controller."""
        controller = getattr(self, "controller", None)
        if controller is None:
            return

        for row_id in self.table.get_children():
            self.table.delete(row_id)

        for row in controller.list_all_orders():
            self.table.insert(
                "",
                "end",
                iid=row[0],
                values=(row[0], row[1], row[2], row[3], row[4]),
            )

    def _on_check_contract(self) -> None:
        """Trigger contract check for the selected order."""
        selection = self.table.selection()
        if not selection:
            return
        self.ctrl.check_contract(int(selection[0]))
