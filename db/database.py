import sqlite3
import os

DEFAULT_DB_FILENAME = "app.sqlite"
DEFAULT_DB_PATH = os.path.join(os.path.dirname(__file__), DEFAULT_DB_FILENAME)

def get_connection(db_path: str = DEFAULT_DB_PATH) -> sqlite3.Connection:
    """Return SQLite connection with foreign keys enabled."""
    if db_path != ":memory:":
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON;")
    conn.row_factory = sqlite3.Row
    return conn
