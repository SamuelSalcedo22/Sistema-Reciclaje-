"""
Módulo responsable de generar reportes estadísticos.

Cruza datos de entregas, materiales y usuarios a través del ReportRepository.
"""
from backend.models import Report
from backend.repositories import ReportRepository


class ReportService:
    """Servicio que genera reportes y métricas del sistema."""

    def __init__(self, report_repo: ReportRepository):
        self._repo = report_repo

    def generate_report(self) -> dict:
        """Genera un reporte completo y lo retorna como diccionario."""
        report = self._repo.generate()
        return report.to_dict()

    def get_summary(self) -> dict:
        """Retorna un resumen compacto del estado del sistema."""
        report = self._repo.generate()
        return {
            "total_usuarios": report.total_users,
            "usuarios_activos": report.active_users,
            "total_entregas": report.total_records,
            "kg_reciclados": round(report.total_kg_recycled, 2),
            "puntos_distribuidos": report.total_points_distributed,
            "solicitudes_pendientes": report.pending_requests,
        }
