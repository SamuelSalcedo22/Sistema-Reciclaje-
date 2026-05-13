"""
Módulo responsable de validar los datos de materiales.
"""
from backend.exceptions import ValidationError
from backend.models.material import VALID_TYPES


class MaterialValidator:
    """Valida los datos de un material antes de persistirlos."""

    @staticmethod
    def validate(name: str, material_type: str, points_per_kg: float) -> None:
        """Lanza ValidationError si los datos no son válidos."""
        if not name or not name.strip():
            raise ValidationError("El nombre del material es obligatorio.")
        if material_type.lower() not in VALID_TYPES:
            raise ValidationError(
                f"Tipo '{material_type}' no válido. Opciones: {', '.join(VALID_TYPES)}"
            )
        if points_per_kg is None or points_per_kg < 0:
            raise ValidationError("Los puntos por kg deben ser un número mayor o igual a 0.")
