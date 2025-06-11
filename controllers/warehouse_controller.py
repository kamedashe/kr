
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
        rows = self.service.list_all()
        self.view.refresh(rows)
        if not rows:
            messagebox.showinfo("Stock", "No components in stock")

    def register_expense(self):
        """Register a component usage expense."""
        try:
            component_id = int(self.view.component_id_var.get())
            qty = int(self.view.qty_var.get())
        except (TypeError, ValueError):
            messagebox.showwarning("Validation", "Component ID and quantity must be numbers")
            return

        if component_id <= 0 or qty <= 0:
            messagebox.showwarning(
                "Validation", "Component ID and quantity must be positive"
            )
            return

        # Adjust stock by negative quantity to represent an expense
        self.service.adjust_stock(component_id, -qty)

        # Refresh the stock view
        self.show_stock()

        messagebox.showinfo("Expense", "Expense registered")
