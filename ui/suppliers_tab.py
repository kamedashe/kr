from tkinter import ttk, StringVar




class SuppliersTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.name_var = StringVar()
        self.contact_var = StringVar()

        self.style = ttk.Style()
        self.style.configure("Error.TEntry", fieldbackground="#ffecec")

        self.build_ui()
        self.populate_suppliers()

    def build_ui(self) -> None:
        """Create widgets for the suppliers tab."""
        form = ttk.Frame(self)
        form.pack(fill="x", pady=5)
        ttk.Label(form, text="Name:").grid(row=0, column=0, padx=5)
        self.name_entry = ttk.Entry(form, textvariable=self.name_var)
        self.name_entry.grid(row=0, column=1, padx=5)
        ttk.Label(form, text="Contact:").grid(row=0, column=2, padx=5)
        ttk.Entry(form, textvariable=self.contact_var).grid(row=0, column=3, padx=5)

        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill="x")
        ttk.Button(btn_frame, text="Add", command=lambda: self.ctrl.on_create()).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Update", command=lambda: self.ctrl.on_update()).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Delete", command=lambda: self.ctrl.on_delete()).pack(side="left", padx=5)

        # Tree with ID column for compatibility with populate_suppliers
        self.tree = ttk.Treeview(self, columns=("id", "name", "contact"), show="headings")
        self.tree.heading("id", text="ID")
        self.tree.heading("name", text="Name")
        self.tree.heading("contact", text="Contact info")
        self.tree.pack(fill="both", expand=True, pady=5)

        # Alias for backward compatibility with controllers using 'table'
        self.table = self.tree

    def set_controller(self, ctrl):
        self.ctrl = ctrl
        self.controller = ctrl

    def highlight_name_field(self, error: bool) -> None:
        style = "Error.TEntry" if error else "TEntry"
        self.name_entry.configure(style=style)

    def refresh(self, suppliers: list[dict]):
        for row in self.table.get_children():
            self.table.delete(row)
        for supplier in suppliers:
            # Skip blank records added accidentally
            if supplier.get("name", "") == "":
                continue
            self.table.insert(
                "",
                "end",
                iid=supplier["id"],
                values=(supplier["name"], supplier["contact_info"]),
            )

    def populate_suppliers(self) -> None:
        """Populate the tree with suppliers from the controller."""
        if not hasattr(self, "tree"):
            return
        for row in self.tree.get_children():
            self.tree.delete(row)

        controller = getattr(self, "controller", None)
        if controller is None:
            return

        for supplier in controller.list_all_suppliers():
            self.tree.insert(
                "",
                "end",
                iid=supplier[0],
                values=(supplier[0], supplier[1], supplier[2]),
            )

