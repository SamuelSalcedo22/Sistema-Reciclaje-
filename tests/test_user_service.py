"""
Módulo de pruebas para UserService.
"""
import unittest
import os
import json
from backend.services import UserService
from backend.repositories import UserRepository
from backend.exceptions import NotFoundError, DuplicateError, ValidationError


class TestUserService(unittest.TestCase):
    """Pruebas unitarias para el servicio de usuarios."""

    def setUp(self):
        """Prepara un archivo JSON temporal para cada test."""
        from backend.storage.database_config import JSON_FILES
        self._original_path = JSON_FILES["users"]
        self._test_path = self._original_path + ".test"
        JSON_FILES["users"] = self._test_path
        # Asegurar archivo limpio
        with open(self._test_path, "w", encoding="utf-8") as f:
            json.dump([], f)
        self.service = UserService(UserRepository())

    def tearDown(self):
        """Limpia el archivo temporal."""
        from backend.storage.database_config import JSON_FILES
        JSON_FILES["users"] = self._original_path
        if os.path.exists(self._test_path):
            os.remove(self._test_path)

    def test_register_user(self):
        dto = self.service.register("Juan Pérez", "juan@correo.com")
        self.assertEqual(dto.name, "Juan Pérez")
        self.assertEqual(dto.email, "juan@correo.com")
        self.assertTrue(dto.active)

    def test_register_invalid_email(self):
        with self.assertRaises(ValidationError):
            self.service.register("Test", "correo_invalido")

    def test_register_empty_name(self):
        with self.assertRaises(ValidationError):
            self.service.register("", "test@mail.com")

    def test_get_by_id(self):
        dto = self.service.register("Ana López", "ana@mail.com")
        found = self.service.get_by_id(dto.id)
        self.assertEqual(found.name, "Ana López")

    def test_get_by_id_not_found(self):
        with self.assertRaises(NotFoundError):
            self.service.get_by_id("id_inexistente")

    def test_get_all(self):
        self.service.register("Uno", "uno@mail.com")
        self.service.register("Dos", "dos@mail.com")
        users = self.service.get_all()
        self.assertEqual(len(users), 2)

    def test_update_user(self):
        dto = self.service.register("Original", "original@mail.com")
        updated = self.service.update(dto.id, "Actualizado", "nuevo@mail.com")
        self.assertEqual(updated.name, "Actualizado")

    def test_deactivate_user(self):
        dto = self.service.register("Activo", "activo@mail.com")
        deactivated = self.service.deactivate(dto.id)
        self.assertFalse(deactivated.active)

    def test_add_points(self):
        dto = self.service.register("Puntos", "puntos@mail.com")
        updated = self.service.add_points(dto.id, 100)
        self.assertEqual(updated.points, 100)

    def test_delete_user(self):
        dto = self.service.register("Borrar", "borrar@mail.com")
        self.service.delete(dto.id)
        with self.assertRaises(NotFoundError):
            self.service.get_by_id(dto.id)

    def test_count(self):
        self.service.register("Ana", "a@mail.com")
        self.service.register("Bob", "b@mail.com")
        self.assertEqual(self.service.count(), 2)


if __name__ == "__main__":
    unittest.main()
