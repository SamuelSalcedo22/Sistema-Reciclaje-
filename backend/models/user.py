"""
Módulo responsable de representar a un usuario en el sistema.

Contiene la entidad de dominio de Usuario.
"""
import uuid
from datetime import datetime


class User:
    """Clase que representa a un usuario participante en el sistema."""

    def __init__(self, name: str, email: str, phone: str = "", address: str = ""):
        self.id: str = str(uuid.uuid4())
        self.name: str = name
        self.email: str = email
        self.phone: str = phone
        self.address: str = address
        self.points: int = 0
        self.registered_at: str = datetime.now().isoformat()
        self.active: bool = True

    def add_points(self, amount: int) -> None:
        """Suma puntos al usuario."""
        if amount > 0:
            self.points += amount

    def to_dict(self) -> dict:
        """Convierte el usuario a diccionario para persistencia."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
            "points": self.points,
            "registered_at": self.registered_at,
            "active": self.active,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        """Crea un User a partir de un diccionario."""
        user = cls(data["name"], data["email"], data.get("phone", ""), data.get("address", ""))
        user.id = data["id"]
        user.points = data.get("points", 0)
        user.registered_at = data.get("registered_at", datetime.now().isoformat())
        user.active = data.get("active", True)
        return user

    def __repr__(self):
        return f"User(id={self.id[:8]}, name={self.name}, points={self.points})"
