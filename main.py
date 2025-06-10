from db.database import get_connection
from ui.main_window import MainWindow
from dao.supplier_dao import SupplierDAO
from services.supplier_service import SupplierService
from controllers.supplier_controller import SupplierController


def main():
    app = MainWindow()
    conn = get_connection()

    supplier_dao = SupplierDAO(conn)
    supplier_service = SupplierService(supplier_dao)
    SupplierController(view=app.suppliers_tab, service=supplier_service)

    app.mainloop()


if __name__ == "__main__":
    main()

