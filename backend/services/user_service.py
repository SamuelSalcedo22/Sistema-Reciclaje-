"""
Módulo responsable de gestionar la lógica de negocio relacionada con los usuarios.

Coordina validaciones, repositorio y DTOs para operaciones CRUD de usuarios.
"""
from backend.models import User
from backend.dtos import UserDTO
from backend.validators import UserValidator
from backend.repositories import UserRepository
from backend.exceptions import NotFoundError


class UserService:
    """Servicio de lógica de negocio para la gestión de usuarios."""

    def __init__(self, repository: UserRepository | None = None):
        self._repo = repository or UserRepository()

    def register(self, name: str, email: str, phone: str = "", address: str = "") -> UserDTO:
        """Registra un nuevo usuario validando sus datos."""
        UserValidator.validate(name, email, phone)
        user = User(name.strip(), email.strip(), phone.strip(), address.strip())
        self._repo.save(user)
        return UserDTO.from_model(user)

    def get_by_id(self, user_id: str) -> UserDTO:
        """Busca un usuario por su ID. Lanza NotFoundError si no existe."""
        user = self._repo.find_by_id(user_id)
        if not user:
            raise NotFoundError("Usuario", user_id)
        return UserDTO.from_model(user)

    def get_all(self) -> list[UserDTO]:
        """Retorna todos los usuarios registrados como DTOs."""
        return [UserDTO.from_model(u) for u in self._repo.get_all()]

    def get_active(self) -> list[UserDTO]:
        """Retorna solo los usuarios activos."""
        return [UserDTO.from_model(u) for u in self._repo.get_active()]

    def update(self, user_id: str, name: str, email: str,
               phone: str = "", address: str = "") -> UserDTO:
        """Actualiza los datos de un usuario existente."""
        user = self._repo.find_by_id(user_id)
        if not user:
            raise NotFoundError("Usuario", user_id)
        UserValidator.validate(name, email, phone)
        user.name = name.strip()
        user.email = email.strip()
        user.phone = phone.strip()
        user.address = address.strip()
        self._repo.update(user)
        return UserDTO.from_model(user)

    def deactivate(self, user_id: str) -> UserDTO:
        """Desactiva un usuario (borrado lógico)."""
        user = self._repo.find_by_id(user_id)
        if not user:
            raise NotFoundError("Usuario", user_id)
        user.active = False
        self._repo.update(user)
        return UserDTO.from_model(user)

    def add_points(self, user_id: str, points: int) -> UserDTO:
        """Agrega puntos a un usuario."""
        user = self._repo.find_by_id(user_id)
        if not user:
            raise NotFoundError("Usuario", user_id)
        user.add_points(points)
        self._repo.update(user)
        return UserDTO.from_model(user)

    def delete(self, user_id: str) -> None:
        """Elimina un usuario permanentemente."""
        self._repo.delete(user_id)

    def count(self) -> int:
        """Retorna el total de usuarios registrados."""
        return self._repo.count()
