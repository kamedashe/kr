import os
from pathlib import Path
from sqlite3 import Connection

from db.database import get_connection, DEFAULT_DB_PATH
from ui.main_window import MainWindow
from controllers.suppliers_controller import SuppliersController
from controllers.orders_controller import OrdersController
from controllers.warehouse_controller import WarehouseController
from facade import Facade


SCHEMA_FILE = Path("db/schema.sql")
SEED_FILE = Path("db/seed.sql")


def _init_db(conn: Connection) -> None:
    """Initialize database schema and seed data."""
    if SCHEMA_FILE.exists():
        with open(SCHEMA_FILE, "r", encoding="utf-8") as f:
            conn.executescript(f.read())
    if SEED_FILE.exists():
        with open(SEED_FILE, "r", encoding="utf-8") as f:
            conn.executescript(f.read())
    conn.commit()


def main() -> None:
    """Application entry point."""
    need_init = not os.path.exists(DEFAULT_DB_PATH)
    conn = get_connection()
    if need_init:
        _init_db(conn)

    facade = Facade(conn)

    app = MainWindow()

    suppliers_ctrl = SuppliersController(app.suppliers_tab)
    orders_ctrl = OrdersController(app.orders_tab)
    warehouse_ctrl = WarehouseController(app.warehouse_tab)

    suppliers_ctrl.facade = facade
    orders_ctrl.facade = facade
    warehouse_ctrl.facade = facade

    app.mainloop()


if __name__ == "__main__":
    main()
