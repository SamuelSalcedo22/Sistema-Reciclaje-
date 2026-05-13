"""
Módulo que implementa una Lista Enlazada Simple (Simple List).

Se utilizará para registros dinámicos o usuarios sin acceso indexado frecuente.
"""


class _Node:
    """Nodo interno de la lista enlazada."""

    def __init__(self, data):
        self.data = data
        self.next = None


class SimpleList:
    """Lista enlazada simple con operaciones básicas."""

    def __init__(self):
        self._head = None
        self._size = 0

    def append(self, data) -> None:
        """Agrega un elemento al final de la lista."""
        new_node = _Node(data)
        if self._head is None:
            self._head = new_node
        else:
            current = self._head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1

    def remove(self, data) -> bool:
        """Elimina la primera ocurrencia del elemento. Retorna True si lo eliminó."""
        current = self._head
        previous = None
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self._head = current.next
                self._size -= 1
                return True
            previous = current
            current = current.next
        return False

    def find(self, predicate) -> object:
        """Retorna el primer elemento que cumpla la condición dada."""
        current = self._head
        while current:
            if predicate(current.data):
                return current.data
            current = current.next
        return None

    def to_list(self) -> list:
        """Convierte la lista enlazada a una lista de Python."""
        result = []
        current = self._head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def is_empty(self) -> bool:
        return self._size == 0

    def size(self) -> int:
        return self._size

    def __iter__(self):
        current = self._head
        while current:
            yield current.data
            current = current.next

    def __len__(self):
        return self._size
