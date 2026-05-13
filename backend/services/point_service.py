"""
Módulo responsable de calcular y asignar puntos a los usuarios.

Basado en el tipo y cantidad de material reciclado.
"""
from backend.repositories import UserRepository, MaterialRepository
from backend.exceptions import NotFoundError


class PointService:
    """Servicio que calcula y asigna puntos según el material y la cantidad."""

    def __init__(self, user_repo: UserRepository, material_repo: MaterialRepository):
        self._user_repo = user_repo
        self._material_repo = material_repo

    def calculate_points(self, material_id: str, quantity_kg: float) -> int:
        """Calcula los puntos correspondientes a una cantidad de material."""
        material = self._material_repo.find_by_id(material_id)
        if not material:
            raise NotFoundError("Material", material_id)
        return int(material.points_per_kg * quantity_kg)

    def award_points(self, user_id: str, material_id: str, quantity_kg: float) -> int:
        """Calcula y asigna puntos a un usuario por una entrega de material."""
        user = self._user_repo.find_by_id(user_id)
        if not user:
            raise NotFoundError("Usuario", user_id)

        points = self.calculate_points(material_id, quantity_kg)
        user.add_points(points)
        self._user_repo.update(user)
        return points
