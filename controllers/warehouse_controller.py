
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
        dto = {
            "component_id": self.view.component_id_var.get(),
            "qty": -abs(self.view.qty_var.get()),
        }
        self.service.create(dto)
        self.view.refresh(self.service.list_all())
