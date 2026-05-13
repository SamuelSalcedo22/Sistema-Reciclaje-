"""
Módulo para la excepción de no encontrado.

Se lanza cuando un recurso solicitado no existe en el sistema.
"""


class NotFoundError(Exception):
    """Excepción lanzada cuando un recurso no existe en el sistema."""

    def __init__(self, resource: str, identifier):
        message = f"No se encontró '{resource}' con identificador: {identifier}"
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"NotFoundError: {self.message}"
