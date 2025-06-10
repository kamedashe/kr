from tkinter import ttk, StringVar




class SuppliersTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.name_var = StringVar()
        self.contact_var = StringVar()

        self.style = ttk.Style()
        self.style.configure("Error.TEntry", fieldbackground="#ffecec")

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

        self.table = ttk.Treeview(self, columns=("name", "contact"), show="headings")
        self.table.heading("name", text="Name")
        self.table.heading("contact", text="Contact info")
        self.table.pack(fill="both", expand=True, pady=5)

    def set_controller(self, ctrl):
        self.ctrl = ctrl

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

