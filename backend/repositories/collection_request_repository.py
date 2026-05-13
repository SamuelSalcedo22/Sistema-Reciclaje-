"""
Módulo responsable de persistir y recuperar solicitudes de recolección.

Utiliza Queue para procesar solicitudes en orden FIFO y ArrayList para
el historial completo.
"""
from backend.data_structures import Queue, ArrayList
from backend.models import CollectionRequest
from backend.models.collection_request import (
    STATUS_PENDING, STATUS_IN_PROGRESS, STATUS_COMPLETED, STATUS_CANCELLED,
)
from backend.storage import JsonStorage, JSON_FILES
from backend.exceptions import NotFoundError


class CollectionRequestRepository:
    """Repositorio que gestiona la persistencia de solicitudes de recolección."""

    def __init__(self):
        self._storage = JsonStorage(JSON_FILES["collection_requests"])
        self._all_requests: ArrayList = ArrayList()
        self._pending_queue: Queue = Queue()
        self._load_from_disk()

    def _load_from_disk(self) -> None:
        """Carga todas las solicitudes del archivo JSON a memoria."""
        for data in self._storage.read_all():
            req = CollectionRequest.from_dict(data)
            self._all_requests.append(req)
            if req.status == STATUS_PENDING:
                self._pending_queue.enqueue(req)

    def _persist(self) -> None:
        """Guarda el estado actual completo al disco."""
        records = [r.to_dict() for r in self._all_requests]
        self._storage.write_all(records)

    def save(self, request: CollectionRequest) -> None:
        """Guarda una nueva solicitud y la agrega a la cola de pendientes."""
        self._all_requests.append(request)
        if request.status == STATUS_PENDING:
            self._pending_queue.enqueue(request)
        self._persist()

    def update_status(self, request_id: str, new_status: str) -> CollectionRequest:
        """Actualiza el estado de una solicitud existente."""
        valid_statuses = (STATUS_PENDING, STATUS_IN_PROGRESS, STATUS_COMPLETED, STATUS_CANCELLED)
        if new_status not in valid_statuses:
            from backend.exceptions import ValidationError
            raise ValidationError(
                f"Estado '{new_status}' no válido. Opciones: {', '.join(valid_statuses)}"
            )
        req = self.find_by_id(request_id)
        if not req:
            raise NotFoundError("Solicitud de recolección", request_id)
        req.update_status(new_status)
        self._persist()
        return req

    def next_pending(self) -> CollectionRequest | None:
        """Retorna y remueve la siguiente solicitud pendiente de la cola."""
        if self._pending_queue.is_empty():
            return None
        return self._pending_queue.dequeue()

    def peek_pending(self) -> CollectionRequest | None:
        """Retorna la siguiente solicitud pendiente sin removerla."""
        return self._pending_queue.peek()

    def find_by_id(self, request_id: str) -> CollectionRequest | None:
        """Busca una solicitud por su ID."""
        return self._all_requests.find(lambda r: r.id == request_id)

    def find_by_user(self, user_id: str) -> list[CollectionRequest]:
        """Retorna todas las solicitudes de un usuario específico."""
        return self._all_requests.filter(lambda r: r.user_id == user_id)

    def get_all(self) -> list[CollectionRequest]:
        """Retorna todas las solicitudes."""
        return self._all_requests.to_list()

    def get_by_status(self, status: str) -> list[CollectionRequest]:
        """Retorna solicitudes filtradas por estado."""
        return self._all_requests.filter(lambda r: r.status == status)

    def pending_count(self) -> int:
        """Retorna la cantidad de solicitudes pendientes en la cola."""
        return self._pending_queue.size()

    def count(self) -> int:
        """Retorna la cantidad total de solicitudes."""
        return self._all_requests.size()
