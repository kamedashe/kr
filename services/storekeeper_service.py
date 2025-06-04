from dao.storekeeper_dao import StorekeeperDAO
from models.storekeeper import Storekeeper

class StorekeeperService:
    """CRUD‑логіка для комірників"""
    def __init__(self, dao: StorekeeperDAO):
        self.dao = dao

    def create(self, keeper: Storekeeper) -> Storekeeper:
        keeper.validate()
        keeper.id = self.dao.insert(keeper)
        return keeper

    def update(self, keeper: Storekeeper) -> bool:
        if keeper.id is None:
            raise ValueError("Storekeeper must have ID before update")
        keeper.validate()
        return self.dao.update(keeper)

    def delete(self, kid: int) -> bool:
        if not isinstance(kid, int):
            raise ValueError("ID must be int")
        return self.dao.delete(kid)

    def get_by_id(self, kid: int) -> Storekeeper | None:
        if not isinstance(kid, int):
            raise ValueError("ID must be int")
        return self.dao.find_by_id(kid)

    def list_all(self) -> list[Storekeeper]:
        return self.dao.find_all()