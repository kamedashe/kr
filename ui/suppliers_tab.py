
from tkinter import ttk, messagebox

class SuppliersTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        lbl = ttk.Label(self, text="SuppliersTab – UI TODO")
        lbl.pack(pady=20)
    def set_controller(self, ctrl): 
        self.ctrl = ctrl
