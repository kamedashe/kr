class SupplierController:
    """Controller for supplier interactions."""

    def __init__(self, view=None, service=None):
        self.view = view
        self.service = service
        if self.view is not None:
            self.view.set_controller(self)

    def _dto_from_view(self) -> dict:
        return {
            "name": self.view.name_var.get(),
            "contact_info": self.view.contact_var.get(),
        }

    def on_create(self):
        dto = self._dto_from_view()
        self.service.create(dto)
        self.view.refresh(self.service.list_all())

    def on_update(self):
        selected = self.view.table.selection()
        if not selected:
            return
        dto = self._dto_from_view()
        dto["id"] = int(selected[0])
        self.service.update(dto)
        self.view.refresh(self.service.list_all())

    def on_delete(self):
        selected = self.view.table.selection()
        if not selected:
            return
        self.service.delete(int(selected[0]))
        self.view.refresh(self.service.list_all())
