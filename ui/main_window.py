
import tkinter as tk
from tkinter import ttk
from ui.reports_tab import ReportsTab
from ui.suppliers_tab import SuppliersTab
from ui.orders_tab import OrdersTab
from ui.warehouse_tab import WarehouseTab

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Система постачання комплектуючих")
        self.geometry("1000x650")

        nb = ttk.Notebook(self)
        nb.pack(fill="both", expand=True)

        self.reports_tab = ReportsTab(nb)
        self.suppliers_tab = SuppliersTab(nb)
        self.orders_tab = OrdersTab(nb)
        self.warehouse_tab = WarehouseTab(nb)

        nb.add(self.reports_tab, text="Звіти")
        nb.add(self.suppliers_tab, text="Постачальники")
        nb.add(self.orders_tab, text="Замовлення")
        nb.add(self.warehouse_tab, text="Склад")
