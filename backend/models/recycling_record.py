"""
Módulo responsable de representar un registro de entrega de reciclaje.

Contiene la entidad de dominio para los registros.
"""
import uuid
from datetime import datetime


class RecyclingRecord:
    """Clase que representa una entrega de material reciclable."""

    def __init__(self, user_id: str, material_id: str, quantity_kg: float, notes: str = ""):
        self.id: str = str(uuid.uuid4())
        self.user_id: str = user_id
        self.material_id: str = material_id
        self.quantity_kg: float = quantity_kg
        self.points_earned: int = 0
        self.notes: str = notes
        self.created_at: str = datetime.now().isoformat()

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "user_id": self.user_id,
            "material_id": self.material_id,
            "quantity_kg": self.quantity_kg,
            "points_earned": self.points_earned,
            "notes": self.notes,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "RecyclingRecord":
        record = cls(data["user_id"], data["material_id"], data["quantity_kg"], data.get("notes", ""))
        record.id = data["id"]
        record.points_earned = data.get("points_earned", 0)
        record.created_at = data.get("created_at", datetime.now().isoformat())
        return record

    def __repr__(self):
        return f"RecyclingRecord(id={self.id[:8]}, user={self.user_id[:8]}, qty={self.quantity_kg}kg)"
