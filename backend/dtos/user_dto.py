"""
Módulo responsable de transferir datos de usuarios.

Evita exponer directamente el modelo de dominio al frontend.
"""


class UserDTO:
    """Objeto simple para transferir información del usuario."""

    def __init__(self, id: str, name: str, email: str, phone: str,
                 address: str, points: int, registered_at: str, active: bool):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.points = points
        self.registered_at = registered_at
        self.active = active

    @classmethod
    def from_model(cls, user) -> "UserDTO":
        return cls(user.id, user.name, user.email, user.phone,
                   user.address, user.points, user.registered_at, user.active)

    def __repr__(self):
        return f"UserDTO(id={self.id[:8]}, name={self.name})"
