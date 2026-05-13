"""
Paquete que contiene las entidades de dominio del sistema.
"""

from .user import User
from .material import Material
from .recycling_record import RecyclingRecord
from .collection_request import CollectionRequest
from .report import Report

__all__ = ["User", "Material", "RecyclingRecord", "CollectionRequest", "Report"]
