
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

        self.table = ttk.Treeview(self, columns=("id", "details"), show="headings")
        self.table.heading("id", text="ID")
        self.table.heading("details", text="Details")
        self.table.pack(fill="both", expand=True)

    def set_controller(self, ctrl):
        self.ctrl = ctrl
        # Alias used by populate_orders for consistency with other tabs
        self.controller = ctrl

    def refresh(self, orders: list[dict]):
        for row in self.table.get_children():
            self.table.delete(row)
        for order in orders:
            self.table.insert("", "end", iid=order["id"], values=(order["id"], order.get("details", "")))

    def populate_orders(self) -> None:
        """Populate the orders table using the attached controller."""
        controller = getattr(self, "controller", None)
        if controller is None:
            return
        for row in self.table.get_children():
            self.table.delete(row)
        for order in controller.list_all_orders():
            details = f"{order['component_id']} x {order['qty']} from {order['supplier_id']}"
            self.table.insert("", "end", iid=order["id"], values=(order["id"], details))

    def _on_check_contract(self) -> None:
        """Trigger contract check for the selected order."""
        selection = self.table.selection()
        if not selection:
            return
        self.ctrl.check_contract(int(selection[0]))
