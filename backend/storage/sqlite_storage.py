"""
Módulo responsable de la persistencia de datos en base de datos SQLite.
"""
import sqlite3
from .database_config import SQLITE_PATH


class SQLiteStorage:
    """Adaptador básico para base de datos SQLite (reservado para uso futuro)."""

    def __init__(self, db_path: str = SQLITE_PATH):
        self._db_path = db_path

    def get_connection(self) -> sqlite3.Connection:
        """Retorna una conexión activa a la base de datos."""
        conn = sqlite3.connect(self._db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def execute(self, query: str, params: tuple = ()) -> list:
        """Ejecuta una consulta y retorna los resultados."""
        with self.get_connection() as conn:
            cursor = conn.execute(query, params)
            return [dict(row) for row in cursor.fetchall()]

    def execute_write(self, query: str, params: tuple = ()) -> int:
        """Ejecuta una escritura y retorna el número de filas afectadas."""
        with self.get_connection() as conn:
            cursor = conn.execute(query, params)
            conn.commit()
            return cursor.rowcount
