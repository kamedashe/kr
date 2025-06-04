import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from db.database import get_connection
from dao.supplier_dao import SupplierDAO
from services.supplier_service import SupplierService
from models.supplier import Supplier

class MockSupplierDAO(SupplierDAO):
    """Заглушка DAO для білого‑ящикового тесту."""
    def __init__(self):
        self.data = {}
        self.auto_id = 1
    def insert(self, supplier: Supplier) -> int:
        supplier.id = self.auto_id
        self.data[self.auto_id] = supplier
        self.auto_id += 1
        return supplier.id
    def find_all(self):
        return list(self.data.values())

def test_create_supplier():
    dao = MockSupplierDAO()
    service = SupplierService(dao)
    supplier = Supplier(name='ACME', contact_info='acme@example.com')
    service.create(supplier)
    assert supplier.id == 1
    assert len(service.list_all()) == 1
