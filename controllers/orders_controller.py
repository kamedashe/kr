from tkinter import Toplevel, ttk, StringVar, IntVar, messagebox


class OrdersController:
    """Controller for purchase orders."""

    def __init__(self, view=None):
        self.view = view
        if self.view is not None:
            self.view.set_controller(self)

    def list_all_orders(self):
        """Return all orders for display."""
        if hasattr(self, "facade"):
            return self.facade.order_dao.list_all()
        return []

    def create_order(self) -> None:
        """Open modal form to create a new order."""
        modal = Toplevel(self.view)
        modal.title("Create order")
        modal.grab_set()

        supplier_var = StringVar()
        component_var = StringVar()
        qty_var = IntVar(value=1)

        suppliers = self.facade.supplier_dao.get_all() if hasattr(self, "facade") else []
        components = self.facade.component_dao.get_all() if hasattr(self, "facade") else []

        ttk.Label(modal, text="Supplier:").grid(row=0, column=0, padx=5, pady=5)
        sup_box = ttk.Combobox(
            modal,
            textvariable=supplier_var,
            state="readonly",
            values=[f"{s['id']} - {s['name']}" for s in suppliers],
        )
        sup_box.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(modal, text="Component:").grid(row=1, column=0, padx=5, pady=5)
        comp_box = ttk.Combobox(
            modal,
            textvariable=component_var,
            state="readonly",
            values=[f"{c['id']} - {c['name']}" for c in components],
        )
        comp_box.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(modal, text="Quantity:").grid(row=2, column=0, padx=5, pady=5)
        ttk.Entry(modal, textvariable=qty_var).grid(row=2, column=1, padx=5, pady=5)

        def on_ok():
            if sup_box.current() == -1 or comp_box.current() == -1:
                messagebox.showwarning("Validation", "Select supplier and component")
                return
            qty = qty_var.get()
            if qty <= 0:
                messagebox.showwarning("Validation", "Quantity must be greater than 0")
                return
            supplier_id = suppliers[sup_box.current()]["id"]
            component_id = components[comp_box.current()]["id"]
            self.facade.order_dao.insert(supplier_id, component_id, qty)
            modal.destroy()
            if hasattr(self.view, "populate_orders"):
                self.view.populate_orders()
            messagebox.showinfo("Order", "Order created")

        ttk.Button(modal, text="OK", command=on_ok).grid(row=3, column=0, columnspan=2, pady=10)

    def check_contract(self, order_id: int) -> None:
        """Show simple contract info for the order."""
        row = self.facade.order_dao.get(order_id) if hasattr(self, "facade") else None
        if not row:
            messagebox.showinfo("Contract", "Order not found")
            return
        message = f"Order #{row['id']}\nSupplier: {row['supplier']}\nDetails: {row['details']}"
        messagebox.showinfo("Contract", message)
