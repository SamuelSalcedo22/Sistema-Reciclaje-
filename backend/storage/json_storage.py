"""
Módulo responsable de la persistencia de datos en archivos JSON.
"""
import json
import os
from typing import List


class JsonStorage:
    """Adaptador para leer y escribir datos en archivos JSON."""

    def __init__(self, filepath: str):
        self._filepath = filepath
        self._ensure_file()

    def _ensure_file(self) -> None:
        """Crea el archivo JSON si no existe."""
        if not os.path.exists(self._filepath):
            with open(self._filepath, "w", encoding="utf-8") as f:
                json.dump([], f)

    def read_all(self) -> List[dict]:
        """Lee y retorna todos los registros."""
        with open(self._filepath, "r", encoding="utf-8") as f:
            return json.load(f)

    def write_all(self, records: List[dict]) -> None:
        """Sobreescribe el archivo con la lista completa de registros."""
        with open(self._filepath, "w", encoding="utf-8") as f:
            json.dump(records, f, ensure_ascii=False, indent=2)

    def save(self, record: dict) -> None:
        """Agrega un nuevo registro o actualiza uno existente por 'id'."""
        records = self.read_all()
        for i, r in enumerate(records):
            if r.get("id") == record.get("id"):
                records[i] = record
                self.write_all(records)
                return
        records.append(record)
        self.write_all(records)

    def delete(self, record_id: str) -> bool:
        """Elimina un registro por su id. Retorna True si existía."""
        records = self.read_all()
        new_records = [r for r in records if r.get("id") != record_id]
        if len(new_records) < len(records):
            self.write_all(new_records)
            return True
        return False

    def find_by_id(self, record_id: str) -> dict | None:
        """Busca y retorna un registro por su id."""
        for r in self.read_all():
            if r.get("id") == record_id:
                return r
        return None
