"""
Módulo responsable de validar los datos de los usuarios.

Comprueba formatos, campos requeridos y reglas de negocio antes de guardar.
"""
import re
from backend.exceptions import ValidationError


class UserValidator:
    """Valida los datos de un usuario antes de persistirlos."""

    EMAIL_REGEX = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$")

    @staticmethod
    def validate(name: str, email: str, phone: str = "") -> None:
        """Lanza ValidationError si los datos no son válidos."""
        if not name or not name.strip():
            raise ValidationError("El nombre del usuario es obligatorio.")
        if len(name.strip()) < 2:
            raise ValidationError("El nombre debe tener al menos 2 caracteres.")
        if not email or not email.strip():
            raise ValidationError("El correo electrónico es obligatorio.")
        if not UserValidator.EMAIL_REGEX.match(email.strip()):
            raise ValidationError(f"El correo '{email}' no tiene un formato válido.")
        if phone and not re.match(r"^[\d\s\+\-\(\)]{7,15}$", phone.strip()):
            raise ValidationError(f"El teléfono '{phone}' no tiene un formato válido.")
