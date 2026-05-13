"""
Módulo responsable de gestionar la lógica de negocio de los materiales reciclables.

Se encarga de crear, listar y administrar tipos de materiales válidos.
"""
from backend.models import Material
from backend.dtos import MaterialDTO
from backend.validators import MaterialValidator
from backend.repositories import MaterialRepository
from backend.exceptions import NotFoundError


class MaterialService:
    """Servicio de lógica de negocio para la gestión de materiales."""

    def __init__(self, repository: MaterialRepository | None = None):
        self._repo = repository or MaterialRepository()

    def create(self, name: str, material_type: str,
               points_per_kg: float, description: str = "") -> MaterialDTO:
        """Crea un nuevo material validando sus datos."""
        MaterialValidator.validate(name, material_type, points_per_kg)
        material = Material(name.strip(), material_type.strip(), points_per_kg, description.strip())
        self._repo.save(material)
        return MaterialDTO.from_model(material)

    def get_by_id(self, material_id: str) -> MaterialDTO:
        """Busca un material por su ID. Lanza NotFoundError si no existe."""
        material = self._repo.find_by_id(material_id)
        if not material:
            raise NotFoundError("Material", material_id)
        return MaterialDTO.from_model(material)

    def get_all(self) -> list[MaterialDTO]:
        """Retorna todos los materiales como DTOs."""
        return [MaterialDTO.from_model(m) for m in self._repo.get_all()]

    def get_active(self) -> list[MaterialDTO]:
        """Retorna solo los materiales activos."""
        return [MaterialDTO.from_model(m) for m in self._repo.get_active()]

    def update(self, material_id: str, name: str, material_type: str,
               points_per_kg: float, description: str = "") -> MaterialDTO:
        """Actualiza un material existente."""
        material = self._repo.find_by_id(material_id)
        if not material:
            raise NotFoundError("Material", material_id)
        MaterialValidator.validate(name, material_type, points_per_kg)
        material.name = name.strip()
        material.material_type = material_type.strip().lower()
        material.points_per_kg = points_per_kg
        material.description = description.strip()
        self._repo.update(material)
        return MaterialDTO.from_model(material)

    def deactivate(self, material_id: str) -> MaterialDTO:
        """Desactiva un material (borrado lógico)."""
        material = self._repo.find_by_id(material_id)
        if not material:
            raise NotFoundError("Material", material_id)
        material.active = False
        self._repo.update(material)
        return MaterialDTO.from_model(material)

    def delete(self, material_id: str) -> None:
        """Elimina un material permanentemente."""
        self._repo.delete(material_id)

    def count(self) -> int:
        """Retorna el total de materiales registrados."""
        return self._repo.count()
