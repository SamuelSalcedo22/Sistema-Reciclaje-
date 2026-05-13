"""
Módulo que implementa una estructura de Cola (Queue).

Se utilizará para procesar solicitudes de recolección en orden de llegada.
"""
from collections import deque


class Queue:
    """Cola FIFO para gestionar solicitudes en orden de llegada."""

    def __init__(self):
        self._data = deque()

    def enqueue(self, item) -> None:
        """Agrega un elemento al final de la cola."""
        self._data.append(item)

    def dequeue(self):
        """Elimina y retorna el elemento del frente. Lanza IndexError si está vacía."""
        if self.is_empty():
            raise IndexError("No se puede extraer de una cola vacía.")
        return self._data.popleft()

    def peek(self):
        """Retorna el elemento del frente sin eliminarlo."""
        if self.is_empty():
            return None
        return self._data[0]

    def to_list(self) -> list:
        return list(self._data)

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def size(self) -> int:
        return len(self._data)

    def __len__(self):
        return len(self._data)
