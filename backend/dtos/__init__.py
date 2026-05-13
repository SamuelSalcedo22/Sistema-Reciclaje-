"""
Paquete que contiene los objetos de transferencia de datos (DTOs).
"""

from .user_dto import UserDTO
from .material_dto import MaterialDTO
from .recycling_record_dto import RecyclingRecordDTO
from .collection_request_dto import CollectionRequestDTO

__all__ = ["UserDTO", "MaterialDTO", "RecyclingRecordDTO", "CollectionRequestDTO"]
