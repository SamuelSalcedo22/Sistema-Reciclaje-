"""
Módulo que implementa una Tabla Hash (Hash Table).

Se utilizará para búsquedas rápidas, como buscar usuarios por ID o correo.
"""


class HashTable:
    """Tabla hash con encadenamiento para manejo de colisiones."""

    def __init__(self, capacity: int = 64):
        self._capacity = capacity
        self._buckets = [[] for _ in range(capacity)]
        self._size = 0

    def _hash(self, key) -> int:
        return hash(key) % self._capacity

    def put(self, key, value) -> None:
        """Inserta o actualiza el par clave-valor."""
        index = self._hash(key)
        bucket = self._buckets[index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self._size += 1

    def get(self, key):
        """Retorna el valor asociado a la clave, o None si no existe."""
        index = self._hash(key)
        for k, v in self._buckets[index]:
            if k == key:
                return v
        return None

    def remove(self, key) -> bool:
        """Elimina la clave y su valor. Retorna True si existía."""
        index = self._hash(key)
        bucket = self._buckets[index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self._size -= 1
                return True
        return False

    def contains(self, key) -> bool:
        return self.get(key) is not None

    def values(self) -> list:
        result = []
        for bucket in self._buckets:
            for _, v in bucket:
                result.append(v)
        return result

    def keys(self) -> list:
        result = []
        for bucket in self._buckets:
            for k, _ in bucket:
                result.append(k)
        return result

    def is_empty(self) -> bool:
        return self._size == 0

    def size(self) -> int:
        return self._size
