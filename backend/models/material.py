"""
Módulo responsable de representar un material reciclable.

Contiene la entidad de dominio de Material.
"""
import uuid

VALID_TYPES = ["plástico", "cartón", "vidrio", "papel", "metal", "orgánico", "otro"]


class Material:
    """Clase que representa un tipo de material reciclable."""

    def __init__(self, name: str, material_type: str, points_per_kg: float, description: str = ""):
        self.id: str = str(uuid.uuid4())
        self.name: str = name
        self.material_type: str = material_type.lower()
        self.points_per_kg: float = points_per_kg
        self.description: str = description
        self.active: bool = True

    def to_dict(self) -> dict:
        """Convierte el material a diccionario para persistencia."""
        return {
            "id": self.id,
            "name": self.name,
            "material_type": self.material_type,
            "points_per_kg": self.points_per_kg,
            "description": self.description,
            "active": self.active,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Material":
        """Crea un Material a partir de un diccionario."""
        mat = cls(data["name"], data["material_type"], data["points_per_kg"], data.get("description", ""))
        mat.id = data["id"]
        mat.active = data.get("active", True)
        return mat

    def __repr__(self):
        return f"Material(id={self.id[:8]}, name={self.name}, type={self.material_type})"
