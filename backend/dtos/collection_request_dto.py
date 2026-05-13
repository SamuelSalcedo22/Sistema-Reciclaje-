"""
Módulo responsable de transferir datos de solicitudes de recolección.
"""


class CollectionRequestDTO:
    """Objeto simple para transferir información de solicitudes."""

    def __init__(self, id: str, user_id: str, address: str, description: str,
                 priority: int, status: str, created_at: str, updated_at: str,
                 user_name: str = ""):
        self.id = id
        self.user_id = user_id
        self.address = address
        self.description = description
        self.priority = priority
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at
        self.user_name = user_name

    @classmethod
    def from_model(cls, req, user_name: str = "") -> "CollectionRequestDTO":
        return cls(req.id, req.user_id, req.address, req.description,
                   req.priority, req.status, req.created_at, req.updated_at, user_name)

    def __repr__(self):
        return f"CollectionRequestDTO(id={self.id[:8]}, status={self.status})"
