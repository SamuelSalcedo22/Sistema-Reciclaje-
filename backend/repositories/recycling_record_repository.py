"""
Módulo responsable de persistir y recuperar registros de entregas de reciclaje.

Utiliza SimpleList (lista enlazada) para almacenamiento dinámico de registros.
"""
from backend.data_structures import SimpleList
from backend.models import RecyclingRecord
from backend.storage import JsonStorage, JSON_FILES
from backend.exceptions import NotFoundError


class RecyclingRecordRepository:
    """Repositorio que gestiona la persistencia de registros de reciclaje."""

    def __init__(self):
        self._storage = JsonStorage(JSON_FILES["recycling_records"])
        self._cache: SimpleList = SimpleList()
        self._load_from_disk()

    def _load_from_disk(self) -> None:
        """Carga todos los registros del archivo JSON a memoria."""
        for data in self._storage.read_all():
            self._cache.append(RecyclingRecord.from_dict(data))

    def _persist(self) -> None:
        """Guarda el estado actual completo al disco."""
        records = [r.to_dict() for r in self._cache]
        self._storage.write_all(records)

    def save(self, record: RecyclingRecord) -> None:
        """Guarda un nuevo registro de reciclaje."""
        self._cache.append(record)
        self._persist()

    def delete(self, record_id: str) -> None:
        """Elimina un registro por su ID."""
        record = self.find_by_id(record_id)
        if not record:
            raise NotFoundError("Registro de reciclaje", record_id)
        self._cache.remove(record)
        self._persist()

    def find_by_id(self, record_id: str) -> RecyclingRecord | None:
        """Busca un registro por su ID."""
        return self._cache.find(lambda r: r.id == record_id)

    def find_by_user(self, user_id: str) -> list[RecyclingRecord]:
        """Retorna todos los registros de un usuario específico."""
        return [r for r in self._cache if r.user_id == user_id]

    def find_by_material(self, material_id: str) -> list[RecyclingRecord]:
        """Retorna todos los registros de un material específico."""
        return [r for r in self._cache if r.material_id == material_id]

    def get_all(self) -> list[RecyclingRecord]:
        """Retorna todos los registros."""
        return self._cache.to_list()

    def count(self) -> int:
        """Retorna la cantidad total de registros."""
        return self._cache.size()

    def total_kg(self) -> float:
        """Retorna el total de kilogramos reciclados."""
        return sum(r.quantity_kg for r in self._cache)

    def total_points(self) -> int:
        """Retorna el total de puntos distribuidos."""
        return sum(r.points_earned for r in self._cache)
