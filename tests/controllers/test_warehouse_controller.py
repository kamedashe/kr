import sqlite3
from types import SimpleNamespace

from controllers.warehouse_controller import WarehouseController
from dao.warehouse_dao import WarehouseDAO
from tkinter import messagebox

class DummyVar:
    def __init__(self, value):
        self.value = value
    def get(self):
        return self.value


def make_controller(comp_id, qty, dao):
    rows_holder = {}
    def populate_stock(rows):
        rows_holder['rows'] = rows
    view = SimpleNamespace(
        component_id_var=DummyVar(comp_id),
        qty_var=DummyVar(qty),
        populate_stock=populate_stock,
        set_controller=lambda x: None,
    )
    ctrl = WarehouseController(view=view)
    ctrl.facade = SimpleNamespace(warehouse_dao=dao)
    return ctrl, rows_holder


def test_register_expense_success(monkeypatch):
    conn = sqlite3.connect(':memory:')
    dao = WarehouseDAO(conn)
    comp_id = dao.insert({'name': 'Bolt', 'unit': 'pcs', 'quantity_in_stock': 5})

    seen = {}
    monkeypatch.setattr(messagebox, 'showinfo', lambda t, m: seen.setdefault('info', m))
    monkeypatch.setattr(messagebox, 'showerror', lambda t, m: seen.setdefault('error', m))

    ctrl, holder = make_controller(comp_id, 3, dao)
    ctrl.register_expense()

    assert 'error' not in seen
    assert 'info' in seen
    assert dao.select_by_id(comp_id)['quantity_in_stock'] == 2
    assert holder['rows'][0][0] == comp_id


def test_register_expense_invalid_qty(monkeypatch):
    conn = sqlite3.connect(':memory:')
    dao = WarehouseDAO(conn)
    comp_id = dao.insert({'name': 'Bolt', 'unit': 'pcs', 'quantity_in_stock': 5})

    seen = {}
    monkeypatch.setattr(messagebox, 'showerror', lambda t, m: seen.setdefault('error', m))

    ctrl, _ = make_controller(comp_id, 0, dao)
    ctrl.register_expense()

    assert 'error' in seen
    assert dao.select_by_id(comp_id)['quantity_in_stock'] == 5


def test_register_expense_insufficient_stock(monkeypatch):
    conn = sqlite3.connect(':memory:')
    dao = WarehouseDAO(conn)
    comp_id = dao.insert({'name': 'Bolt', 'unit': 'pcs', 'quantity_in_stock': 1})

    seen = {}
    monkeypatch.setattr(messagebox, 'showerror', lambda t, m: seen.setdefault('error', m))

    ctrl, _ = make_controller(comp_id, 2, dao)
    ctrl.register_expense()

    assert 'error' in seen
    assert dao.select_by_id(comp_id)['quantity_in_stock'] == 1
