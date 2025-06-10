from dao.component_dao import ComponentDAO


class ComponentService:
    """Business logic for components using dict DTOs."""

    def __init__(self, dao: ComponentDAO):
        self.dao = dao

    def create(self, dto: dict) -> int:
        return self.dao.insert(dto)

    def update(self, dto: dict) -> bool:
        return self.dao.update(dto)

    def delete(self, component_id: int) -> bool:
        return self.dao.delete(component_id)

    def list_all(self) -> list[dict]:
        return self.dao.select_all()

    def get(self, component_id: int) -> dict | None:
        """Return component by ID."""
        return self.dao.select_by_id(component_id)

    def adjust_stock(self, component_id: int, delta: int) -> None:
        self.dao.update_quantity(component_id, delta)
