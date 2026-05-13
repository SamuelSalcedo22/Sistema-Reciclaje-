"""
Módulo responsable de gestionar las solicitudes de recolección.

Prioriza y organiza las solicitudes usando la estructura Queue.
"""
from backend.models import CollectionRequest
from backend.dtos import CollectionRequestDTO
from backend.validators import CollectionValidator
from backend.repositories import CollectionRequestRepository, UserRepository
from backend.exceptions import NotFoundError


class CollectionService:
    """Servicio de lógica de negocio para solicitudes de recolección."""

    def __init__(self, collection_repo: CollectionRequestRepository | None = None,
                 user_repo: UserRepository | None = None):
        self._collection_repo = collection_repo or CollectionRequestRepository()
        self._user_repo = user_repo or UserRepository()

    def create_request(self, user_id: str, address: str,
                       description: str = "", priority: int = 1) -> CollectionRequestDTO:
        """Crea una nueva solicitud de recolección."""
        CollectionValidator.validate(user_id, address, priority)

        # Verificar que el usuario exista
        user = self._user_repo.find_by_id(user_id)
        if not user:
            raise NotFoundError("Usuario", user_id)

        request = CollectionRequest(user_id, address.strip(), description.strip(), priority)
        self._collection_repo.save(request)
        return CollectionRequestDTO.from_model(request, user.name)

    def process_next(self) -> CollectionRequestDTO | None:
        """Procesa la siguiente solicitud pendiente de la cola."""
        request = self._collection_repo.next_pending()
        if not request:
            return None
        self._collection_repo.update_status(request.id, "en_proceso")
        user = self._user_repo.find_by_id(request.user_id)
        return CollectionRequestDTO.from_model(
            request, user.name if user else "Desconocido"
        )

    def complete_request(self, request_id: str) -> CollectionRequestDTO:
        """Marca una solicitud como completada."""
        req = self._collection_repo.update_status(request_id, "completada")
        user = self._user_repo.find_by_id(req.user_id)
        return CollectionRequestDTO.from_model(
            req, user.name if user else "Desconocido"
        )

    def cancel_request(self, request_id: str) -> CollectionRequestDTO:
        """Cancela una solicitud."""
        req = self._collection_repo.update_status(request_id, "cancelada")
        user = self._user_repo.find_by_id(req.user_id)
        return CollectionRequestDTO.from_model(
            req, user.name if user else "Desconocido"
        )

    def get_all(self) -> list[CollectionRequestDTO]:
        """Retorna todas las solicitudes como DTOs."""
        results = []
        for req in self._collection_repo.get_all():
            user = self._user_repo.find_by_id(req.user_id)
            results.append(CollectionRequestDTO.from_model(
                req, user.name if user else "Desconocido"
            ))
        return results

    def get_by_user(self, user_id: str) -> list[CollectionRequestDTO]:
        """Retorna las solicitudes de un usuario específico."""
        requests = self._collection_repo.find_by_user(user_id)
        return [CollectionRequestDTO.from_model(r) for r in requests]

    def get_pending(self) -> list[CollectionRequestDTO]:
        """Retorna todas las solicitudes pendientes."""
        pending = self._collection_repo.get_by_status("pendiente")
        return [CollectionRequestDTO.from_model(r) for r in pending]

    def pending_count(self) -> int:
        """Retorna la cantidad de solicitudes pendientes."""
        return self._collection_repo.pending_count()

    def count(self) -> int:
        """Retorna el total de solicitudes."""
        return self._collection_repo.count()
