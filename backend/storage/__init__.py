"""
Paquete que maneja la configuración y adaptadores de almacenamiento de datos.
"""

from .json_storage import JsonStorage
from .database_config import JSON_FILES

__all__ = ["JsonStorage", "JSON_FILES"]
