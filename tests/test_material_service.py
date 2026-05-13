"""
Módulo de pruebas para MaterialService.
"""
import unittest
import os
import json
from backend.services import MaterialService
from backend.repositories import MaterialRepository
from backend.exceptions import NotFoundError, ValidationError


class TestMaterialService(unittest.TestCase):
    """Pruebas unitarias para el servicio de materiales."""

    def setUp(self):
        from backend.storage.database_config import JSON_FILES
        self._original_path = JSON_FILES["materials"]
        self._test_path = self._original_path + ".test"
        JSON_FILES["materials"] = self._test_path
        with open(self._test_path, "w", encoding="utf-8") as f:
            json.dump([], f)
        self.service = MaterialService(MaterialRepository())

    def tearDown(self):
        from backend.storage.database_config import JSON_FILES
        JSON_FILES["materials"] = self._original_path
        if os.path.exists(self._test_path):
            os.remove(self._test_path)

    def test_create_material(self):
        dto = self.service.create("Botella PET", "plástico", 10.0, "Botellas de plástico")
        self.assertEqual(dto.name, "Botella PET")
        self.assertEqual(dto.material_type, "plástico")
        self.assertEqual(dto.points_per_kg, 10.0)

    def test_create_invalid_type(self):
        with self.assertRaises(ValidationError):
            self.service.create("Algo", "tipo_invalido", 5.0)

    def test_create_negative_points(self):
        with self.assertRaises(ValidationError):
            self.service.create("Algo", "vidrio", -1.0)

    def test_get_by_id(self):
        dto = self.service.create("Cartón", "cartón", 8.0)
        found = self.service.get_by_id(dto.id)
        self.assertEqual(found.name, "Cartón")

    def test_get_by_id_not_found(self):
        with self.assertRaises(NotFoundError):
            self.service.get_by_id("inexistente")

    def test_get_all(self):
        self.service.create("M1", "vidrio", 5.0)
        self.service.create("M2", "papel", 3.0)
        materials = self.service.get_all()
        self.assertEqual(len(materials), 2)

    def test_deactivate(self):
        dto = self.service.create("Temp", "metal", 15.0)
        deactivated = self.service.deactivate(dto.id)
        self.assertFalse(deactivated.active)

    def test_delete(self):
        dto = self.service.create("Borrar", "orgánico", 2.0)
        self.service.delete(dto.id)
        with self.assertRaises(NotFoundError):
            self.service.get_by_id(dto.id)


if __name__ == "__main__":
    unittest.main()
