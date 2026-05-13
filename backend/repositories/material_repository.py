"""
Módulo responsable de persistir y recuperar datos de materiales.

Utiliza ArrayList para almacenamiento con acceso indexado rápido.
"""
from backend.data_structures import ArrayList
from backend.models import Material
from backend.storage import JsonStorage, JSON_FILES
from backend.exceptions import NotFoundError, DuplicateError


class MaterialRepository:
    """Repositorio que gestiona la persistencia de materiales reciclables."""

    def __init__(self):
        self._storage = JsonStorage(JSON_FILES["materials"])
        self._cache: ArrayList = ArrayList()
        self._load_from_disk()

    def _load_from_disk(self) -> None:
        """Carga todos los materiales del archivo JSON a memoria."""
        for data in self._storage.read_all():
            self._cache.append(Material.from_dict(data))

    def _persist(self) -> None:
        """Guarda el estado actual completo al disco."""
        records = [m.to_dict() for m in self._cache]
        self._storage.write_all(records)

    def save(self, material: Material) -> None:
        """Guarda un material nuevo. Lanza DuplicateError si el nombre ya existe."""
        existing = self.find_by_name(material.name)
        if existing and existing.id != material.id:
            raise DuplicateError("Material", material.name)
        self._cache.append(material)
        self._persist()

    def update(self, material: Material) -> None:
        """Actualiza un material existente."""
        for i in range(self._cache.size()):
            if self._cache.get(i).id == material.id:
                self._cache.remove_at(i)
                self._cache.append(material)
                self._persist()
                return
        raise NotFoundError("Material", material.id)

    def delete(self, material_id: str) -> None:
        """Elimina un material por su ID."""
        mat = self.find_by_id(material_id)
        if not mat:
            raise NotFoundError("Material", material_id)
        self._cache.remove(mat)
        self._persist()

    def find_by_id(self, material_id: str) -> Material | None:
        """Busca un material por su ID."""
        return self._cache.find(lambda m: m.id == material_id)

    def find_by_name(self, name: str) -> Material | None:
        """Busca un material por su nombre (case-insensitive)."""
        name_lower = name.lower()
        return self._cache.find(lambda m: m.name.lower() == name_lower)

    def get_all(self) -> list[Material]:
        """Retorna todos los materiales registrados."""
        return self._cache.to_list()

    def get_active(self) -> list[Material]:
        """Retorna solo los materiales activos."""
        return self._cache.filter(lambda m: m.active)

    def count(self) -> int:
        """Retorna la cantidad total de materiales."""
        return self._cache.size()
