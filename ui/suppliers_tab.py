from tkinter import ttk, StringVar


class SuppliersTab(ttk.Frame):
    """Tab displaying suppliers."""

    def __init__(self, parent):
        super().__init__(parent)
        self.name_var = StringVar()
        self.contact_var = StringVar()
        self._build_ui()
        self.populate_suppliers()

    def _build_ui(self) -> None:
        form = ttk.Frame(self)
        form.pack(fill="x", pady=5)
        ttk.Label(form, text="Name:").grid(row=0, column=0, padx=5)
        ttk.Entry(form, textvariable=self.name_var).grid(row=0, column=1, padx=5)
        ttk.Label(form, text="Contact:").grid(row=0, column=2, padx=5)
        ttk.Entry(form, textvariable=self.contact_var).grid(row=0, column=3, padx=5)

        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill="x", pady=5)
        ttk.Button(btn_frame, text="Add", command=lambda: self.ctrl.on_create()).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Update", command=lambda: self.ctrl.on_update()).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Delete", command=lambda: self.ctrl.on_delete()).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Supply history", command=self._on_history).pack(side="left", padx=5)

        columns = ("id", "name", "contact")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")
        self.tree.pack(fill="both", expand=True)
        self.table = self.tree

    def set_controller(self, ctrl):
        self.ctrl = ctrl
        self.controller = ctrl

    def refresh(self, suppliers):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for s in suppliers:
            self.tree.insert("", "end", iid=s["id"], values=(s["id"], s["name"], s.get("contact", "")))

    def populate_suppliers(self):
        controller = getattr(self, "controller", None)
        if controller is None:
            return
        self.refresh(controller.list_all_suppliers())

    def _on_history(self) -> None:
        selection = self.tree.selection()
        if not selection:
            return
        self.ctrl.show_supply_history(int(selection[0]))
