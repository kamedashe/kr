from db.database import get_connection
from ui.main_window import MainWindow
from dao.supplier_dao import SupplierDAO
from services.supplier_service import SupplierService
from controllers.supplier_controller import SupplierController
from dao.history_dao import HistoryDAO
from services.history_service import HistoryService
from services.report_service import ReportService
from controllers.report_controller import ReportController
from services.component_service import ComponentService
from dao.component_dao import ComponentDAO
from controllers.warehouse_controller import WarehouseController


def main():
    app = MainWindow()
    conn = get_connection()

    supplier_dao = SupplierDAO(conn)
    supplier_service = SupplierService(supplier_dao)
    SupplierController(view=app.suppliers_tab, service=supplier_service)

    component_service = ComponentService(ComponentDAO(conn))
    WarehouseController(view=app.warehouse_tab, service=component_service)

    report_service = ReportService()
    history_service = HistoryService(HistoryDAO(conn))
    ReportController(app.reports_tab, report_service, history_service)

    app.mainloop()


if __name__ == "__main__":
    main()

