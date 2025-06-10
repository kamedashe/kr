from db.database import get_connection
from ui.main_window import MainWindow
from dao.supplier_dao import SupplierDAO
from services.supplier_service import SupplierService
from controllers.suppliers_controller import SuppliersController
from dao.history_dao import HistoryDAO
from services.history_service import HistoryService
from services.report_service import ReportService
from controllers.reports_controller import ReportsController
from services.warehouse_service import WarehouseService
from dao.warehouse_dao import WarehouseDAO
from services.order_service import OrderService
from services.contract_service import ContractService
from dao.order_dao import OrderDAO
from dao.contract_dao import ContractDAO
from controllers.warehouse_controller import WarehouseController
from controllers.orders_controller import OrdersController


def main():
    app = MainWindow()
    conn = get_connection()

    reports_tab = app.reports_tab
    suppliers_tab = app.suppliers_tab
    orders_tab = app.orders_tab
    warehouse_tab = app.warehouse_tab

    reports_ctrl = ReportsController(
        view=reports_tab,
        report_service=ReportService(),
        history_service=HistoryService(HistoryDAO(conn)),
    )

    suppliers_ctrl = SuppliersController(
        view=suppliers_tab,
        service=SupplierService(SupplierDAO(conn)),
    )

    warehouse_ctrl = WarehouseController(
        warehouse_tab,
        WarehouseService(WarehouseDAO(conn)),
    )

    orders_ctrl = OrdersController(
        orders_tab,
        OrderService(OrderDAO(conn)),
        ContractService(ContractDAO(conn)),
    )

    app.mainloop()


if __name__ == "__main__":
    main()

