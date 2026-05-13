"""
Paquete que contiene las estructuras de datos propias del sistema.
"""

from .simple_list import SimpleList
from .array_list import ArrayList
from .hash_table import HashTable
from .queue import Queue
from .stack import Stack
from .set_registry import SetRegistry

__all__ = ["SimpleList", "ArrayList", "HashTable", "Queue", "Stack", "SetRegistry"]
