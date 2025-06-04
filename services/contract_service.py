from dao.supplier_dao import SupplierDAO

class ContractService:
    """Фасад для валідації контрактів постачальників."""
    def __init__(self, supplier_dao: SupplierDAO):
        self.supplier_dao = supplier_dao

    def validate_contract(self, supplier_id: int):
        """Може перевіряти, чи постачальник має всі необхідні дані для контракту."""
        supplier = self.supplier_dao.find_by_id(supplier_id)
        # Тут може бути додаткова логіка
        return supplier is not None and supplier.contact_info != ""
