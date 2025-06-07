import tkinter as tk
from tkinter import ttk

from .component_tab import ComponentTab
from .supplier_tab import SupplierTab
from .warehouse_tab import WarehouseTab
from .storekeeper_tab import StorekeeperTab
from .supply_tab import SupplyTab


class MainWindow:
    """TODO: Main window with tabs"""

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("IS Dept Complectation")
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill="both")

        self.component_tab = ComponentTab(self.notebook)
        self.supplier_tab = SupplierTab(self.notebook)
        self.warehouse_tab = WarehouseTab(self.notebook)
        self.storekeeper_tab = StorekeeperTab(self.notebook)
        self.supply_tab = SupplyTab(self.notebook)

        self.notebook.add(self.component_tab.frame, text="Комплектуючі")
        self.notebook.add(self.supplier_tab.frame, text="Постачальники")
        self.notebook.add(self.warehouse_tab.frame, text="Склади")
        self.notebook.add(self.storekeeper_tab.frame, text="Комірники")
        self.notebook.add(self.supply_tab.frame, text="Поставки")
