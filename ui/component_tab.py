import tkinter as tk
from tkinter import ttk


class ComponentTab:
    """TODO: UI for components"""

    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.tree = ttk.Treeview(self.frame)
        self.tree.pack(expand=True, fill="both")
        self.form = ttk.Frame(self.frame)
        self.form.pack()
        # TODO: add fields
        pass
