"""
Módulo responsable de representar una solicitud de recolección de residuos.

Contiene la entidad de dominio correspondiente.
"""
import uuid
from datetime import datetime

STATUS_PENDING = "pendiente"
STATUS_IN_PROGRESS = "en_proceso"
STATUS_COMPLETED = "completada"
STATUS_CANCELLED = "cancelada"


class CollectionRequest:
    """Clase que representa una solicitud para recolección."""

    def __init__(self, user_id: str, address: str, description: str = "", priority: int = 1):
        self.id: str = str(uuid.uuid4())
        self.user_id: str = user_id
        self.address: str = address
        self.description: str = description
        self.priority: int = priority
        self.status: str = STATUS_PENDING
        self.created_at: str = datetime.now().isoformat()
        self.updated_at: str = datetime.now().isoformat()

    def update_status(self, new_status: str) -> None:
        """Actualiza el estado de la solicitud."""
        self.status = new_status
        self.updated_at = datetime.now().isoformat()

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "user_id": self.user_id,
            "address": self.address,
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "CollectionRequest":
        req = cls(data["user_id"], data["address"], data.get("description", ""), data.get("priority", 1))
        req.id = data["id"]
        req.status = data.get("status", STATUS_PENDING)
        req.created_at = data.get("created_at", datetime.now().isoformat())
        req.updated_at = data.get("updated_at", datetime.now().isoformat())
        return req

    def __repr__(self):
        return f"CollectionRequest(id={self.id[:8]}, status={self.status})"
