"""
Módulo responsable de persistir y recuperar datos de usuarios.

Utiliza HashTable para búsquedas rápidas por ID y SetRegistry para
garantizar unicidad de correos electrónicos.
"""
from backend.data_structures import HashTable, SetRegistry
from backend.models import User
from backend.storage import JsonStorage, JSON_FILES
from backend.exceptions import NotFoundError, DuplicateError


class UserRepository:
    """Repositorio que gestiona la persistencia de usuarios."""

    def __init__(self):
        self._storage = JsonStorage(JSON_FILES["users"])
        self._cache: HashTable = HashTable()
        self._email_registry: SetRegistry = SetRegistry()
        self._load_from_disk()

    def _load_from_disk(self) -> None:
        """Carga todos los usuarios del archivo JSON a memoria."""
        for data in self._storage.read_all():
            user = User.from_dict(data)
            self._cache.put(user.id, user)
            self._email_registry.add(user.email.lower())

    def _persist(self) -> None:
        """Guarda el estado actual completo al disco."""
        records = [u.to_dict() for u in self._cache.values()]
        self._storage.write_all(records)

    def save(self, user: User) -> None:
        """Guarda un usuario nuevo. Lanza DuplicateError si el correo ya existe."""
        if self._email_registry.contains(user.email.lower()):
            existing = self.find_by_email(user.email)
            if existing and existing.id != user.id:
                raise DuplicateError("Usuario", user.email)
        self._cache.put(user.id, user)
        self._email_registry.add(user.email.lower())
        self._persist()

    def update(self, user: User) -> None:
        """Actualiza un usuario existente."""
        if not self._cache.contains(user.id):
            raise NotFoundError("Usuario", user.id)
        self._cache.put(user.id, user)
        self._persist()

    def delete(self, user_id: str) -> None:
        """Elimina un usuario por su ID."""
        user = self.find_by_id(user_id)
        if not user:
            raise NotFoundError("Usuario", user_id)
        self._email_registry.remove(user.email.lower())
        self._cache.remove(user_id)
        self._persist()

    def find_by_id(self, user_id: str) -> User | None:
        """Busca un usuario por su ID."""
        return self._cache.get(user_id)

    def find_by_email(self, email: str) -> User | None:
        """Busca un usuario por su correo electrónico."""
        email_lower = email.lower()
        for user in self._cache.values():
            if user.email.lower() == email_lower:
                return user
        return None

    def get_all(self) -> list[User]:
        """Retorna todos los usuarios registrados."""
        return self._cache.values()

    def get_active(self) -> list[User]:
        """Retorna solo los usuarios activos."""
        return [u for u in self._cache.values() if u.active]

    def count(self) -> int:
        """Retorna la cantidad total de usuarios."""
        return self._cache.size()
