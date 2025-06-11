from tkinter import messagebox


class WarehouseController:
    """Controller for warehouse-related actions."""

    def __init__(self, view=None, service=None):
        self.view = view
        self.service = service
        if self.view is not None:
            self.view.set_controller(self)

    def show_stock(self):
        """Load current stock data into the view."""
        self.view.refresh(self.service.list_all())

    def register_expense(self):
        """Register a component usage expense."""
        component_id = self.view.component_id_var.get()
        qty = self.view.qty_var.get()

        if component_id <= 0 or qty <= 0:
            messagebox.showerror(
                "Validation", "Component ID and quantity must be positive"
            )
            return

        try:
            self.service.register_expense(component_id, qty)
        except ValueError as exc:
            messagebox.showerror("Error", str(exc))
            return

        self.view.refresh(self.service.list_all())
        messagebox.showinfo("Success", "Expense registered")
