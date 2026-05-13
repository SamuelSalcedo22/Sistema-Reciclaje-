"""
Módulo responsable de la lógica para registrar y procesar entregas de reciclaje.

Calcula cantidades, se comunica con el servicio de puntos y persiste los registros.
"""
from backend.models import RecyclingRecord
from backend.dtos import RecyclingRecordDTO
from backend.validators import RecyclingValidator
from backend.repositories import (
    RecyclingRecordRepository, UserRepository, MaterialRepository,
)
from backend.services.point_service import PointService
from backend.exceptions import NotFoundError


class RecyclingService:
    """Servicio de lógica de negocio para entregas de reciclaje."""

    def __init__(self, recycling_repo: RecyclingRecordRepository | None = None,
                 user_repo: UserRepository | None = None,
                 material_repo: MaterialRepository | None = None):
        self._recycling_repo = recycling_repo or RecyclingRecordRepository()
        self._user_repo = user_repo or UserRepository()
        self._material_repo = material_repo or MaterialRepository()
        self._point_service = PointService(self._user_repo, self._material_repo)

    def register_delivery(self, user_id: str, material_id: str,
                          quantity_kg: float, notes: str = "") -> RecyclingRecordDTO:
        """Registra una nueva entrega de material reciclable."""
        RecyclingValidator.validate(user_id, material_id, quantity_kg)

        # Verificar que existan el usuario y el material
        user = self._user_repo.find_by_id(user_id)
        if not user:
            raise NotFoundError("Usuario", user_id)
        material = self._material_repo.find_by_id(material_id)
        if not material:
            raise NotFoundError("Material", material_id)

        # Crear registro y calcular puntos
        record = RecyclingRecord(user_id, material_id, quantity_kg, notes.strip())
        points = self._point_service.award_points(user_id, material_id, quantity_kg)
        record.points_earned = points

        self._recycling_repo.save(record)

        return RecyclingRecordDTO.from_model(record, user.name, material.name)

    def get_by_id(self, record_id: str) -> RecyclingRecordDTO:
        """Busca un registro por su ID."""
        record = self._recycling_repo.find_by_id(record_id)
        if not record:
            raise NotFoundError("Registro de reciclaje", record_id)
        user = self._user_repo.find_by_id(record.user_id)
        material = self._material_repo.find_by_id(record.material_id)
        return RecyclingRecordDTO.from_model(
            record,
            user.name if user else "Desconocido",
            material.name if material else "Desconocido",
        )

    def get_all(self) -> list[RecyclingRecordDTO]:
        """Retorna todos los registros como DTOs con nombres resueltos."""
        results = []
        for record in self._recycling_repo.get_all():
            user = self._user_repo.find_by_id(record.user_id)
            material = self._material_repo.find_by_id(record.material_id)
            results.append(RecyclingRecordDTO.from_model(
                record,
                user.name if user else "Desconocido",
                material.name if material else "Desconocido",
            ))
        return results

    def get_by_user(self, user_id: str) -> list[RecyclingRecordDTO]:
        """Retorna los registros de un usuario específico."""
        records = self._recycling_repo.find_by_user(user_id)
        return [RecyclingRecordDTO.from_model(r) for r in records]

    def delete(self, record_id: str) -> None:
        """Elimina un registro de reciclaje."""
        self._recycling_repo.delete(record_id)

    def count(self) -> int:
        """Retorna el total de registros."""
        return self._recycling_repo.count()
