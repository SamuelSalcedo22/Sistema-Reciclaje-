"""
Módulo de pruebas para CollectionService.
"""
import unittest
import os
import json
from backend.services import CollectionService
from backend.repositories import CollectionRequestRepository, UserRepository
from backend.exceptions import NotFoundError, ValidationError


class TestCollectionService(unittest.TestCase):
    """Pruebas unitarias para el servicio de recolección."""

    def setUp(self):
        from backend.storage.database_config import JSON_FILES
        self._originals = {k: v for k, v in JSON_FILES.items()}
        for key in ("users", "collection_requests"):
            test_path = JSON_FILES[key] + ".test"
            JSON_FILES[key] = test_path
            with open(test_path, "w", encoding="utf-8") as f:
                json.dump([], f)

        self._user_repo = UserRepository()
        self._collection_repo = CollectionRequestRepository()

        from backend.models import User
        self._user = User("Recolector", "recolector@mail.com", address="Calle 123")
        self._user_repo.save(self._user)

        self.service = CollectionService(self._collection_repo, self._user_repo)

    def tearDown(self):
        from backend.storage.database_config import JSON_FILES
        for key, original in self._originals.items():
            test_path = JSON_FILES[key]
            JSON_FILES[key] = original
            if os.path.exists(test_path):
                os.remove(test_path)

    def test_create_request(self):
        dto = self.service.create_request(
            self._user.id, "Avenida Principal 456", "Residuos plásticos", 2,
        )
        self.assertEqual(dto.address, "Avenida Principal 456")
        self.assertEqual(dto.status, "pendiente")
        self.assertEqual(dto.priority, 2)

    def test_create_invalid_address(self):
        with self.assertRaises(ValidationError):
            self.service.create_request(self._user.id, "AB")

    def test_create_invalid_priority(self):
        with self.assertRaises(ValidationError):
            self.service.create_request(self._user.id, "Dirección válida", priority=5)

    def test_process_next(self):
        self.service.create_request(self._user.id, "Dirección uno")
        self.service.create_request(self._user.id, "Dirección dos")
        processed = self.service.process_next()
        self.assertIsNotNone(processed)
        self.assertEqual(processed.address, "Dirección uno")
        self.assertEqual(processed.status, "en_proceso")

    def test_process_next_empty(self):
        result = self.service.process_next()
        self.assertIsNone(result)

    def test_complete_request(self):
        dto = self.service.create_request(self._user.id, "Calle completar")
        completed = self.service.complete_request(dto.id)
        self.assertEqual(completed.status, "completada")

    def test_cancel_request(self):
        dto = self.service.create_request(self._user.id, "Calle cancelar")
        cancelled = self.service.cancel_request(dto.id)
        self.assertEqual(cancelled.status, "cancelada")

    def test_get_pending(self):
        self.service.create_request(self._user.id, "Pendiente uno")
        self.service.create_request(self._user.id, "Pendiente dos")
        pending = self.service.get_pending()
        self.assertEqual(len(pending), 2)

    def test_pending_count(self):
        self.service.create_request(self._user.id, "Solicitud A")
        self.assertEqual(self.service.pending_count(), 1)


if __name__ == "__main__":
    unittest.main()
