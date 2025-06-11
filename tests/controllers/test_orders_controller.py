import sqlite3
from types import SimpleNamespace

from controllers.orders_controller import OrdersController
from dao.order_dao import OrderDAO
from tkinter import messagebox


def test_check_contract(monkeypatch):
    conn = sqlite3.connect(':memory:')
    # create required tables
    conn.execute('CREATE TABLE suppliers (id INTEGER PRIMARY KEY, name TEXT)')
    conn.execute('CREATE TABLE components (id INTEGER PRIMARY KEY, name TEXT)')
    conn.execute("INSERT INTO suppliers (name) VALUES ('ACME')")
    conn.execute("INSERT INTO components (name) VALUES ('Bolt')")

    dao = OrderDAO(conn)
    order_id = dao.insert({'supplier_id': 1, 'component_id': 1, 'qty': 2})

    ctrl = OrdersController()
    ctrl.facade = SimpleNamespace(order_dao=dao)

    seen = {}

    def fake_showinfo(title, message):
        seen['title'] = title
        seen['message'] = message

    monkeypatch.setattr(messagebox, 'showinfo', fake_showinfo)

    ctrl.check_contract(order_id)

    assert 'Order #' in seen['message']
    assert 'ACME' in seen['message']

