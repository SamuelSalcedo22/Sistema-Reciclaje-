"""
Paquete que contiene las excepciones personalizadas del sistema.
"""

from .validation_error import ValidationError
from .not_found_error import NotFoundError
from .duplicate_error import DuplicateError

__all__ = ["ValidationError", "NotFoundError", "DuplicateError"]
