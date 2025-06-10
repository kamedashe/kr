
from tkinter import ttk, messagebox

class WarehouseTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        lbl = ttk.Label(self, text="WarehouseTab – UI TODO")
        lbl.pack(pady=20)
    def set_controller(self, ctrl): 
        self.ctrl = ctrl
