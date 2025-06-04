import sqlite3
import os

# Шлях за замовчуванням
DEFAULT_DB_FILENAME = "supply.db"
DEFAULT_DB_PATH = os.path.join(os.path.dirname(__file__), DEFAULT_DB_FILENAME)

def get_connection(db_path: str = DEFAULT_DB_PATH) -> sqlite3.Connection:
    """
    Повертає підключення до SQLite, з увімкненими foreign_keys
    і row_factory=sqlite3.Row.
    Параметр db_path дозволяє вказати шлях до іншої БД (для тестування).
    """
    if db_path != ":memory:":
        # Переконаємося, що директорія існує (якщо БД у підпапці)
        os.makedirs(os.path.dirname(db_path), exist_ok=True)

    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON;")
    conn.row_factory = sqlite3.Row
    return conn
