class OrdersController:
    """Controller for purchase orders."""

    def __init__(self, view=None, order_service=None, contract_service=None):
        """Initialize controller with optional services and view."""
        self.view = view
        self.order_service = order_service
        self.contract_service = contract_service

        if self.view is not None:
            self.view.set_controller(self)

    def list_all_orders(self) -> list[dict]:
        """Return all orders using the facade DAO if available."""
        if hasattr(self, "facade"):
            try:
                return self.facade.order_dao.select_all()
            except Exception:
                return []
        return []

    def create_order(self):
        """Create a new purchase order via a simple modal form."""
        from tkinter import Toplevel, ttk, StringVar, IntVar, messagebox, Listbox, MULTIPLE

        modal = Toplevel(self.view)
        modal.title("Create order")
        modal.grab_set()

        supplier_var = StringVar()
        qty_var = IntVar(value=1)

        suppliers = []
        components = []
        if hasattr(self, "facade"):
            try:
                suppliers = self.facade.supplier_dao.select_all()
            except Exception:
                suppliers = []
            try:
                components = self.facade.component_dao.select_all()
            except Exception:
                components = []

        ttk.Label(modal, text="Supplier:").grid(row=0, column=0, padx=5, pady=5)
        supplier_cb = ttk.Combobox(
            modal,
            textvariable=supplier_var,
            state="readonly",
            values=[f"{s['id']} - {s['name']}" for s in suppliers],
        )
        supplier_cb.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(modal, text="Components:").grid(row=1, column=0, padx=5, pady=5)
        comp_list = Listbox(modal, selectmode=MULTIPLE, height=5)
        for c in components:
            comp_list.insert("end", f"{c['id']} - {c['name']}")
        comp_list.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(modal, text="Quantity:").grid(row=2, column=0, padx=5, pady=5)
        ttk.Entry(modal, textvariable=qty_var).grid(row=2, column=1, padx=5, pady=5)

        def on_ok():
            qty = qty_var.get()
            if qty <= 0:
                messagebox.showwarning("Validation", "Quantity must be greater than 0")
                return

            indices = comp_list.curselection()
            if not indices:
                messagebox.showwarning("Validation", "Select at least one component")
                return

            if supplier_cb.current() == -1:
                messagebox.showwarning("Validation", "Select supplier")
                return

            # Simplified: use only the first selected component
            component_id = components[indices[0]]["id"]
            supplier_id = suppliers[supplier_cb.current()]["id"]

            if hasattr(self, "facade"):
                self.facade.order_dao.insert(
                    {
                        "supplier_id": supplier_id,
                        "component_id": component_id,
                        "qty": qty,
                    }
                )

            modal.destroy()
            if hasattr(self.view, "populate_orders"):
                self.view.populate_orders()
            messagebox.showinfo("Order", "Order created")

        ttk.Button(modal, text="OK", command=on_ok).grid(row=3, column=0, columnspan=2, pady=10)

    def check_contract(self):
        """Placeholder for contract checking logic."""
        if self.contract_service is not None:
            try:
                contracts = self.contract_service.list_all()
            except Exception:
                contracts = []
        else:
            contracts = []

        if self.view is not None:
            self.view.refresh(contracts)

