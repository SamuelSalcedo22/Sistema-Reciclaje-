"""
Módulo responsable de validar las solicitudes de recolección.
"""
from backend.exceptions import ValidationError


class CollectionValidator:
    """Valida los datos de una solicitud de recolección."""

    @staticmethod
    def validate(user_id: str, address: str, priority: int = 1) -> None:
        """Lanza ValidationError si los datos no son válidos."""
        if not user_id:
            raise ValidationError("El usuario es obligatorio para la solicitud.")
        if not address or not address.strip():
            raise ValidationError("La dirección de recolección es obligatoria.")
        if len(address.strip()) < 5:
            raise ValidationError("La dirección debe tener al menos 5 caracteres.")
        if priority not in (1, 2, 3):
            raise ValidationError("La prioridad debe ser 1 (baja), 2 (media) o 3 (alta).")
