import tkinter as tk
from tkinter import messagebox
from db.database import get_connection
from dao.component_dao import ComponentDAO
from services.component_service import ComponentService
from models.component import Component

class ComponentWindow:
    def __init__(self, root: tk.Toplevel | tk.Tk):
        self.root = root
        self.root.title("Комплектуючі")
        self.center_window(400, 300)

        conn = get_connection()
        self.service = ComponentService(ComponentDAO(conn))

        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True)


        # Поля вводу
        tk.Label(self.frame, text="Назва:").grid(row=0, column=0, sticky="e")
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=2)

        tk.Label(self.frame, text="Одиниця виміру:").grid(row=1, column=0, sticky="e")
        self.unit_entry = tk.Entry(self.frame)
        self.unit_entry.grid(row=1, column=1, padx=5, pady=2)

        # Кнопки
        self.add_button = tk.Button(self.frame, text="Додати", width=12, command=self.add)
        self.add_button.grid(row=2, column=0, padx=5, pady=5)

        self.edit_button = tk.Button(self.frame, text="Редагувати", width=12, command=self.edit)
        self.edit_button.grid(row=2, column=1, padx=5, pady=5)

        self.delete_button = tk.Button(self.frame, text="Видалити", width=12, command=self.delete)
        self.delete_button.grid(row=3, column=0, columnspan=2, pady=5)

        self.listbox = tk.Listbox(self.frame, width=50)
        self.listbox.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

        self.refresh()

    def center_window(self, width=400, height=300):
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    # ---------------------------- CRUD ---------------------------
    def add(self):
        name = self.name_entry.get().strip()
        unit = self.unit_entry.get().strip()
        if not name or not unit:
            messagebox.showwarning("Помилка", "Усі поля мають бути заповнені.")
            return
        try:
            self.service.create(Component(name=name, unit=unit))
            self._clear_inputs()
            self.refresh()
        except ValueError as err:
            messagebox.showerror("Помилка", str(err))

    def edit(self):
        comp_id = self._selected_id()
        if comp_id is None:
            return
        comp = self.service.get_by_id(comp_id)
        # Наповнити поля
        self.name_entry.delete(0, tk.END)
        self.unit_entry.delete(0, tk.END)
        self.name_entry.insert(0, comp.name)
        self.unit_entry.insert(0, comp.unit)
        # Перевизначити кнопку
        self.add_button.config(text="Зберегти", command=lambda cid=comp_id: self.save(cid))

    def save(self, comp_id: int):
        name = self.name_entry.get().strip()
        unit = self.unit_entry.get().strip()
        try:
            current_qty = self.service.get_by_id(comp_id).quantity_in_stock
            self.service.update(Component(id=comp_id, name=name, unit=unit, quantity_in_stock=current_qty))
        except ValueError as err:
            messagebox.showerror("Помилка", str(err))
            return
        # reset
        self.add_button.config(text="Додати", command=self.add)
        self._clear_inputs()
        self.refresh()

    def delete(self):
        comp_id = self._selected_id()
        if comp_id is None:
            return
        if messagebox.askyesno("Підтвердження", "Видалити компонент?"):
            self.service.delete(comp_id)
            self.refresh()

    # ---------------------------- helpers ------------------------
    def refresh(self):
        self.listbox.delete(0, tk.END)
        for c in self.service.list_all():
            self.listbox.insert(tk.END, f"{c.id}. {c.name} ({c.unit}) | {c.quantity_in_stock}")

    def _clear_inputs(self):
        self.name_entry.delete(0, tk.END)
        self.unit_entry.delete(0, tk.END)

    def _selected_id(self) -> int | None:
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showwarning("Виберіть", "Оберіть елемент зі списку.")
            return None
        return int(self.listbox.get(sel[0]).split('.')[0])
