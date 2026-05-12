"""
controllers/
Intermediario entre la UI y la lógica de negocio (Backend).
Aquí se concentran las acciones disparadas por botones y la futura
comunicación con APIs o servicios de datos.
"""

from __future__ import annotations

from typing import Any, Callable


class MainController:
    """Orquesta navegación y operaciones; las vistas solo invocan estos métodos."""

    def __init__(self, app: Any) -> None:
        self._app = app
        self._dashboard_refresh_callback: Callable[[], None] | None = None

    def set_dashboard_refresh_handler(self, handler: Callable[[], None]) -> None:
        """Permite al dashboard registrar cómo actualizar sus etiquetas al refrescar."""
        self._dashboard_refresh_callback = handler

    def navigate_to(self, view_name: str) -> None:
        self._app.show_view(view_name)

    def refresh_dashboard(self) -> None:
        """Simula recarga de datos; en producción consultaría al backend."""
        if self._dashboard_refresh_callback:
            self._dashboard_refresh_callback()

    def register_user_placeholder(self) -> None:
        """Reservado: enviar formulario de usuario al backend."""
        pass

    def save_material_placeholder(self) -> None:
        """Reservado: persistir catálogo de materiales."""
        pass

    def approve_collection_placeholder(self) -> None:
        """Reservado: aprobar solicitud de recolección."""
        pass
