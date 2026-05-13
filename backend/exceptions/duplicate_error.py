"""
Módulo para la excepción de duplicado.

Se lanza cuando se intenta registrar algo que ya existe (ej: mismo correo).
"""


class DuplicateError(Exception):
    """Excepción lanzada cuando se intenta insertar un recurso duplicado."""

    def __init__(self, resource: str, identifier):
        message = f"Ya existe un '{resource}' con el identificador: {identifier}"
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"DuplicateError: {self.message}"
