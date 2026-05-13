"""
Módulo de pruebas para RecyclingService.
"""
import unittest
import os
import json
from backend.services import RecyclingService
from backend.repositories import (
    RecyclingRecordRepository, UserRepository, MaterialRepository,
)
from backend.exceptions import NotFoundError, ValidationError


class TestRecyclingService(unittest.TestCase):
    """Pruebas unitarias para el servicio de reciclaje."""

    def setUp(self):
        from backend.storage.database_config import JSON_FILES
        self._originals = {k: v for k, v in JSON_FILES.items()}
        for key in ("users", "materials", "recycling_records"):
            test_path = JSON_FILES[key] + ".test"
            JSON_FILES[key] = test_path
            with open(test_path, "w", encoding="utf-8") as f:
                json.dump([], f)

        self._user_repo = UserRepository()
        self._material_repo = MaterialRepository()
        self._recycling_repo = RecyclingRecordRepository()

        # Crear datos de prueba
        from backend.models import User, Material
        self._user = User("Tester", "tester@mail.com")
        self._user_repo.save(self._user)

        self._material = Material("PET", "plástico", 10.0)
        self._material_repo.save(self._material)

        self.service = RecyclingService(
            self._recycling_repo, self._user_repo, self._material_repo,
        )

    def tearDown(self):
        from backend.storage.database_config import JSON_FILES
        for key, original in self._originals.items():
            test_path = JSON_FILES[key]
            JSON_FILES[key] = original
            if os.path.exists(test_path):
                os.remove(test_path)

    def test_register_delivery(self):
        dto = self.service.register_delivery(
            self._user.id, self._material.id, 5.0, "Primera entrega",
        )
        self.assertEqual(dto.quantity_kg, 5.0)
        self.assertEqual(dto.points_earned, 50)  # 5kg * 10 pts/kg
        self.assertEqual(dto.user_name, "Tester")

    def test_register_delivery_invalid_quantity(self):
        with self.assertRaises(ValidationError):
            self.service.register_delivery(self._user.id, self._material.id, 0)

    def test_register_delivery_user_not_found(self):
        with self.assertRaises(NotFoundError):
            self.service.register_delivery("fake_id", self._material.id, 1.0)

    def test_get_all(self):
        self.service.register_delivery(self._user.id, self._material.id, 2.0)
        self.service.register_delivery(self._user.id, self._material.id, 3.0)
        records = self.service.get_all()
        self.assertEqual(len(records), 2)

    def test_points_accumulate(self):
        self.service.register_delivery(self._user.id, self._material.id, 5.0)
        self.service.register_delivery(self._user.id, self._material.id, 3.0)
        user = self._user_repo.find_by_id(self._user.id)
        self.assertEqual(user.points, 80)  # (5+3)*10


if __name__ == "__main__":
    unittest.main()
