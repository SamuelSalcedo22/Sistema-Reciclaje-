"""
Módulo que implementa un Conjunto (Set).

Se utilizará para evitar duplicados en registros o identificadores.
"""


class SetRegistry:
    """Conjunto que evita elementos duplicados."""

    def __init__(self):
        self._data = set()

    def add(self, item) -> bool:
        """Agrega un elemento. Retorna True si fue agregado, False si ya existía."""
        if item in self._data:
            return False
        self._data.add(item)
        return True

    def remove(self, item) -> bool:
        """Elimina un elemento. Retorna True si existía."""
        if item in self._data:
            self._data.remove(item)
            return True
        return False

    def contains(self, item) -> bool:
        return item in self._data

    def to_list(self) -> list:
        return list(self._data)

    def size(self) -> int:
        return len(self._data)

    def is_empty(self) -> bool:
        return len(self._data) == 0
