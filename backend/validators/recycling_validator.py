"""
Módulo responsable de validar los registros de reciclaje.
"""
from backend.exceptions import ValidationError


class RecyclingValidator:
    """Valida los datos de una entrega de reciclaje."""

    @staticmethod
    def validate(user_id: str, material_id: str, quantity_kg: float) -> None:
        """Lanza ValidationError si los datos no son válidos."""
        if not user_id:
            raise ValidationError("El usuario es obligatorio para registrar una entrega.")
        if not material_id:
            raise ValidationError("El material es obligatorio para registrar una entrega.")
        if quantity_kg is None or quantity_kg <= 0:
            raise ValidationError("La cantidad en kg debe ser mayor a 0.")
        if quantity_kg > 10000:
            raise ValidationError("La cantidad ingresada supera el límite permitido (10,000 kg).")
