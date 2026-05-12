"""
Módulo que implementa una Lista basada en Arreglos (Array List).

Se utilizará para materiales o registros donde las búsquedas sean frecuentes.
"""


class ArrayList:
    """
    Implementación de una lista basada en arreglos (Array List).
    Permite el acceso indexado rápido y crece dinámicamente.
    """
    def __init__(self, initial_capacity=10):
        self._capacity = initial_capacity
        self._size = 0
        self._items = [None] * self._capacity

    def add(self, item):
        """Agrega un elemento al final de la lista."""
        if self._size == self._capacity:
            self._resize()
        self._items[self._size] = item
        self._size += 1

    def _resize(self):
        """Duplica la capacidad del arreglo interno."""
        self._capacity *= 2
        new_items = [None] * self._capacity
        for i in range(self._size):
            new_items[i] = self._items[i]
        self._items = new_items

    def get(self, index):
        """Obtiene el elemento en el índice especificado."""
        if not 0 <= index < self._size:
            raise IndexError("Índice fuera de rango")
        return self._items[index]

    def set(self, index, item):
        """Reemplaza el elemento en el índice especificado."""
        if not 0 <= index < self._size:
            raise IndexError("Índice fuera de rango")
        self._items[index] = item

    def remove(self, index):
        """Elimina y retorna el elemento en el índice especificado."""
        if not 0 <= index < self._size:
            raise IndexError("Índice fuera de rango")
        removed_item = self._items[index]
        for i in range(index, self._size - 1):
            self._items[i] = self._items[i+1]
        self._items[self._size - 1] = None
        self._size -= 1
        return removed_item

    def size(self):
        """Retorna el número de elementos en la lista."""
        return self._size

    def is_empty(self):
        """Retorna True si la lista está vacía."""
        return self._size == 0

    def clear(self):
        """Limpia la lista."""
        self._items = [None] * self._capacity
        self._size = 0

    def __iter__(self):
        for i in range(self._size):
            yield self._items[i]

    def __str__(self):
        elements = [str(self._items[i]) for i in range(self._size)]
        return "[" + ", ".join(elements) + "]"

    def __repr__(self):
        return self.__str__()

