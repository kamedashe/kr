from controllers.supplier_controller import SupplierController
from tkinter import messagebox, Toplevel, ttk


class SuppliersController(SupplierController):
    """Alias controller matching naming convention."""

    def list_all_suppliers(self) -> list[tuple[int, str, str]]:
        """Return all suppliers ordered by ``id`` ascending."""
        return self.facade.supplier_dao.get_all()

    def show_supply_history(self, supplier_id: int) -> None:
        """Display supply history for the given supplier in a modal window."""
        rows = self.facade.supply_dao.get_history_by_supplier(supplier_id)
        if not rows:
            messagebox.showinfo("Report", "No supply history available")
            return

        modal = Toplevel(self.view)
        modal.title("Supply history")
        modal.resizable(True, True)
        modal.grab_set()

        columns = ("date", "component", "qty")
        tree = ttk.Treeview(modal, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center")
        for date, component, qty in rows:
            tree.insert("", "end", values=(date, component, qty))

        scrollbar = ttk.Scrollbar(modal, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
