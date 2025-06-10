from tkinter import messagebox


class OrdersController:
    """Controller for purchase orders."""

    def __init__(self, view=None, order_service=None, contract_service=None):
        self.view = view
        self.order_service = order_service
        self.contract_service = contract_service
        if self.view is not None:
            self.view.set_controller(self)

    def create_order(self):
        """Create a new order using details from the view."""
        dto = {"details": self.view.details_var.get()}
        orders = []
        if self.order_service is not None:
            self.order_service.create(dto)
            orders = self.order_service.list_all()
        if self.view is not None:
            self.view.refresh(orders)

    def check_contract(self):
        """Verify the selected order's contract status."""
        sel = self.view.table.selection()
        if not sel:
            return
        order_id = int(sel[0])
        ok = False
        if self.contract_service is not None:
            ok = self.contract_service.verify(order_id)
        messagebox.showinfo("Contract", "Completed" if ok else "Not completed")

