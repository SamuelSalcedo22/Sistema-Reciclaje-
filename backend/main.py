"""
Punto de entrada principal del backend.

Configura la inicialización de repositorios y servicios, y los expone
como un contenedor centralizado de dependencias.
"""
from backend.repositories import (
    UserRepository,
    MaterialRepository,
    RecyclingRecordRepository,
    CollectionRequestRepository,
    ReportRepository,
)
from backend.services import (
    UserService,
    MaterialService,
    RecyclingService,
    CollectionService,
    ReportService,
)


class AppContainer:
    """Contenedor de dependencias del sistema.

    Inicializa todos los repositorios y servicios compartiendo instancias
    para garantizar consistencia de datos en memoria.
    """

    def __init__(self):
        # Repositorios (capa de datos)
        self.user_repo = UserRepository()
        self.material_repo = MaterialRepository()
        self.recycling_repo = RecyclingRecordRepository()
        self.collection_repo = CollectionRequestRepository()
        self.report_repo = ReportRepository(
            self.user_repo, self.material_repo,
            self.recycling_repo, self.collection_repo,
        )

        # Servicios (capa de negocio)
        self.user_service = UserService(self.user_repo)
        self.material_service = MaterialService(self.material_repo)
        self.recycling_service = RecyclingService(
            self.recycling_repo, self.user_repo, self.material_repo,
        )
        self.collection_service = CollectionService(
            self.collection_repo, self.user_repo,
        )
        self.report_service = ReportService(self.report_repo)


def create_app() -> AppContainer:
    """Crea y retorna el contenedor de la aplicación."""
    return AppContainer()
