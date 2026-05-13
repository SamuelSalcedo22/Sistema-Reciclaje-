"""
Paquete que maneja el acceso y la persistencia de datos.
"""

from .user_repository import UserRepository
from .material_repository import MaterialRepository
from .recycling_record_repository import RecyclingRecordRepository
from .collection_request_repository import CollectionRequestRepository
from .report_repository import ReportRepository

__all__ = [
    "UserRepository",
    "MaterialRepository",
    "RecyclingRecordRepository",
    "CollectionRequestRepository",
    "ReportRepository",
]
