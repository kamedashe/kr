from dao.component_dao import ComponentDAO
from models.component import Component

class ComponentService:
    """Сервісний шар для роботи з компонентами (комплектуючими).

    Інкапсулює CRUD-операції та базову бізнес-логіку, щоби GUI або інші
    модулі не взаємодіяли з DAO безпосередньо.
    """

    def __init__(self, dao: ComponentDAO):
        self.dao = dao

    # ------------------------------------------------------------------
    # CRUD
    # ------------------------------------------------------------------
    def create(self, component: Component) -> Component:
        """Додає новий компонент у БД і повертає його з установленим id."""
        component.validate()
        component.id = self.dao.insert(component)
        return component

    def update(self, component: Component) -> bool:
        """Оновлює дані компонента. Повертає True, якщо 1 рядок змінено."""
        if component.id is None:
            raise ValueError("Component must have an ID to be updated.")
        component.validate()
        return self.dao.update(component)

    def delete(self, component_id: int) -> bool:
        """Видаляє компонент за id. Повертає True, якщо 1 рядок видалено."""
        self._check_id(component_id)
        return self.dao.delete(component_id)
    
    def get_by_id(self, component_id: int) -> Component | None:
        return self.dao.find_by_id(component_id)

    def list_all(self) -> list[Component]:
        return self.dao.find_all()


    # ------------------------------------------------------------------
    # Stock operations (optional business-logic helpers)
    # ------------------------------------------------------------------
    def increment_stock(self, component_id: int, delta: int) -> None:
        """Збільшує (або зменшує, якщо delta < 0) кількість на складі."""
        self._check_id(component_id)
        if not isinstance(delta, int):
            raise ValueError("Delta must be an integer.")
        self.dao.update_quantity(component_id, delta)

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------
    def _check_id(self, value: int):
        if not isinstance(value, int):
            raise ValueError("ID must be an integer.")
