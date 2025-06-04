from services.contract_service import ContractService
from dao.contract_dao import ContractDAO

class MockContractDAO(ContractDAO):
    def find_by_id(self, contract_id):
        if contract_id == 1:
            class Contract: contact_info = "info"
            return Contract()
        return None

def test_validate_contract_true():
    dao = MockContractDAO()
    service = ContractService(dao)
    assert service.validate_contract(1) is True

def test_validate_contract_false():
    dao = MockContractDAO()
    service = ContractService(dao)
    assert service.validate_contract(9999) is False
