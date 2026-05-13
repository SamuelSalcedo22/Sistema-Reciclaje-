"""
Módulo responsable de generar reportes a partir de los repositorios.

No persiste datos propios; genera reportes bajo demanda.
"""
from backend.models import Report


class ReportRepository:
    """Generador de reportes del sistema (solo lectura, sin persistencia propia)."""

    def __init__(self, user_repo, material_repo, recycling_repo, collection_repo):
        self._user_repo = user_repo
        self._material_repo = material_repo
        self._recycling_repo = recycling_repo
        self._collection_repo = collection_repo

    def generate(self) -> Report:
        """Genera un reporte completo con métricas del sistema."""
        report = Report()

        all_users = self._user_repo.get_all()
        report.total_users = len(all_users)
        report.active_users = len([u for u in all_users if u.active])

        report.total_records = self._recycling_repo.count()
        report.total_kg_recycled = self._recycling_repo.total_kg()
        report.total_points_distributed = self._recycling_repo.total_points()

        report.pending_requests = self._collection_repo.pending_count()

        # Resumen por tipo de material
        materials_summary = {}
        all_materials = self._material_repo.get_all()
        for material in all_materials:
            records = self._recycling_repo.find_by_material(material.id)
            total_kg = sum(r.quantity_kg for r in records)
            total_pts = sum(r.points_earned for r in records)
            if total_kg > 0:
                materials_summary[material.name] = {
                    "type": material.material_type,
                    "total_kg": round(total_kg, 2),
                    "total_points": total_pts,
                    "deliveries": len(records),
                }
        report.materials_summary = materials_summary

        return report
