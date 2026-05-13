"""
Módulo responsable de la configuración general de la base de datos o sistema de archivos.
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, "data")

os.makedirs(DATA_DIR, exist_ok=True)

JSON_FILES = {
    "users": os.path.join(DATA_DIR, "users.json"),
    "materials": os.path.join(DATA_DIR, "materials.json"),
    "recycling_records": os.path.join(DATA_DIR, "recycling_records.json"),
    "collection_requests": os.path.join(DATA_DIR, "collection_requests.json"),
}

SQLITE_PATH = os.path.join(DATA_DIR, "ecogestor.db")
