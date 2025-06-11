from tkinter import messagebox


class WarehouseController:
    """Controller providing stock information and expense registration."""

    def __init__(self, view=None):
        self.view = view
        if self.view is not None:
            self.view.set_controller(self)

    def show_stock(self) -> None:
        """Populate the stock table in the attached view."""
        rows = []
        if hasattr(self, "facade"):
            try:
                rows = self.facade.warehouse_dao.get_all_stock()
            except Exception:
                rows = []
        if self.view:
            self.view.populate_stock(rows)

    def register_expense(self) -> None:
        """Validate fields and register component expense."""
        try:
            component_id = int(self.view.component_id_var.get())
            qty = int(self.view.qty_var.get())
        except Exception:
            messagebox.showerror("Error", "Invalid input")
            return

        if qty <= 0:
            messagebox.showerror("Error", "Quantity must be greater than 0")
            return

        if hasattr(self, "facade"):
            try:
                self.facade.warehouse_dao.register_expense(component_id, qty)
            except ValueError as exc:
                messagebox.showerror("Error", str(exc))
                return

        self.show_stock()
        messagebox.showinfo("Success", "Expense registered")
