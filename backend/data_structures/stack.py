"""
Módulo que implementa una estructura de Pila (Stack).

Se utilizará para historial de acciones o para deshacer cambios.
"""


class Stack:
    """Pila LIFO para historial de operaciones."""

    def __init__(self):
        self._data = []

    def push(self, item) -> None:
        """Agrega un elemento en la cima."""
        self._data.append(item)

    def pop(self):
        """Elimina y retorna el elemento de la cima. Lanza IndexError si está vacía."""
        if self.is_empty():
            raise IndexError("No se puede extraer de una pila vacía.")
        return self._data.pop()

    def peek(self):
        """Retorna el elemento de la cima sin eliminarlo."""
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def size(self) -> int:
        return len(self._data)

    def __len__(self):
        return len(self._data)
