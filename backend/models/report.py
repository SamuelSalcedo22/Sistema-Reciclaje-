"""
Módulo responsable de representar un reporte de participación y materiales.

Contiene la entidad o estructura para datos de reportes.
"""
from datetime import datetime


class Report:
    """Clase que representa un resumen o reporte del sistema."""

    def __init__(self):
        self.generated_at: str = datetime.now().isoformat()
        self.total_users: int = 0
        self.active_users: int = 0
        self.total_records: int = 0
        self.total_kg_recycled: float = 0.0
        self.total_points_distributed: int = 0
        self.pending_requests: int = 0
        self.materials_summary: dict = {}

    def to_dict(self) -> dict:
        return {
            "generated_at": self.generated_at,
            "total_users": self.total_users,
            "active_users": self.active_users,
            "total_records": self.total_records,
            "total_kg_recycled": self.total_kg_recycled,
            "total_points_distributed": self.total_points_distributed,
            "pending_requests": self.pending_requests,
            "materials_summary": self.materials_summary,
        }

    def __repr__(self):
        return f"Report(generated={self.generated_at}, kg={self.total_kg_recycled})"
