"""
Módulo que implementa una Lista basada en Arreglos (Array List).

Se utilizará para materiales o registros donde las búsquedas sean frecuentes.
"""


class ArrayList:
    """Lista dinámica basada en arreglo con acceso indexado O(1)."""

    def __init__(self):
        self._data = []

    def append(self, item) -> None:
        """Agrega un elemento al final."""
        self._data.append(item)

    def get(self, index: int):
        """Retorna el elemento en la posición dada."""
        if index < 0 or index >= len(self._data):
            raise IndexError(f"Índice {index} fuera de rango.")
        return self._data[index]

    def remove_at(self, index: int) -> None:
        """Elimina el elemento en la posición dada."""
        if index < 0 or index >= len(self._data):
            raise IndexError(f"Índice {index} fuera de rango.")
        self._data.pop(index)

    def remove(self, item) -> bool:
        """Elimina la primera ocurrencia del elemento."""
        if item in self._data:
            self._data.remove(item)
            return True
        return False

    def find(self, predicate) -> object:
        """Retorna el primer elemento que cumpla la condición."""
        for item in self._data:
            if predicate(item):
                return item
        return None

    def filter(self, predicate) -> list:
        """Retorna todos los elementos que cumplan la condición."""
        return [item for item in self._data if predicate(item)]

    def to_list(self) -> list:
        return list(self._data)

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def size(self) -> int:
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)
