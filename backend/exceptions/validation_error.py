"""
Módulo para la excepción de error de validación.

Se lanza cuando los datos no cumplen con las reglas requeridas.
"""


class ValidationError(Exception):
    """Excepción lanzada cuando los datos no superan la validación."""

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"ValidationError: {self.message}"
