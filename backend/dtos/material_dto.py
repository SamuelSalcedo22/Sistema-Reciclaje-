"""
Módulo responsable de transferir datos de materiales.
"""


class MaterialDTO:
    """Objeto simple para transferir información de un material."""

    def __init__(self, id: str, name: str, material_type: str,
                 points_per_kg: float, description: str, active: bool):
        self.id = id
        self.name = name
        self.material_type = material_type
        self.points_per_kg = points_per_kg
        self.description = description
        self.active = active

    @classmethod
    def from_model(cls, material) -> "MaterialDTO":
        return cls(material.id, material.name, material.material_type,
                   material.points_per_kg, material.description, material.active)

    def __repr__(self):
        return f"MaterialDTO(id={self.id[:8]}, name={self.name})"
