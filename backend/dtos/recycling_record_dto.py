"""
Módulo responsable de transferir datos de registros de reciclaje.
"""


class RecyclingRecordDTO:
    """Objeto simple para transferir información de entregas."""

    def __init__(self, id: str, user_id: str, material_id: str,
                 quantity_kg: float, points_earned: int, notes: str,
                 created_at: str, user_name: str = "", material_name: str = ""):
        self.id = id
        self.user_id = user_id
        self.material_id = material_id
        self.quantity_kg = quantity_kg
        self.points_earned = points_earned
        self.notes = notes
        self.created_at = created_at
        self.user_name = user_name
        self.material_name = material_name

    @classmethod
    def from_model(cls, record, user_name: str = "", material_name: str = "") -> "RecyclingRecordDTO":
        return cls(record.id, record.user_id, record.material_id,
                   record.quantity_kg, record.points_earned, record.notes,
                   record.created_at, user_name, material_name)

    def __repr__(self):
        return f"RecyclingRecordDTO(id={self.id[:8]}, qty={self.quantity_kg}kg)"
