"""
Módulo de pruebas para las estructuras de datos propias.
"""
import unittest
from backend.data_structures import SimpleList, ArrayList, HashTable, Queue, Stack, SetRegistry


class TestSimpleList(unittest.TestCase):
    """Pruebas para la lista enlazada simple."""

    def setUp(self):
        self.lista = SimpleList()

    def test_append_and_size(self):
        self.lista.append("a")
        self.lista.append("b")
        self.assertEqual(self.lista.size(), 2)

    def test_remove_existing(self):
        self.lista.append("x")
        self.assertTrue(self.lista.remove("x"))
        self.assertEqual(self.lista.size(), 0)

    def test_remove_non_existing(self):
        self.assertFalse(self.lista.remove("nada"))

    def test_find(self):
        self.lista.append(10)
        self.lista.append(20)
        result = self.lista.find(lambda x: x > 15)
        self.assertEqual(result, 20)

    def test_find_not_found(self):
        self.lista.append(1)
        self.assertIsNone(self.lista.find(lambda x: x > 100))

    def test_to_list(self):
        self.lista.append("a")
        self.lista.append("b")
        self.assertEqual(self.lista.to_list(), ["a", "b"])

    def test_iter(self):
        self.lista.append(1)
        self.lista.append(2)
        self.assertEqual(list(self.lista), [1, 2])

    def test_is_empty(self):
        self.assertTrue(self.lista.is_empty())
        self.lista.append(1)
        self.assertFalse(self.lista.is_empty())


class TestArrayList(unittest.TestCase):
    """Pruebas para la lista basada en arreglo."""

    def setUp(self):
        self.lista = ArrayList()

    def test_append_and_get(self):
        self.lista.append("primero")
        self.assertEqual(self.lista.get(0), "primero")

    def test_get_out_of_range(self):
        with self.assertRaises(IndexError):
            self.lista.get(0)

    def test_remove_at(self):
        self.lista.append("a")
        self.lista.append("b")
        self.lista.remove_at(0)
        self.assertEqual(self.lista.get(0), "b")

    def test_remove_item(self):
        self.lista.append("x")
        self.assertTrue(self.lista.remove("x"))
        self.assertEqual(self.lista.size(), 0)

    def test_find(self):
        self.lista.append(5)
        self.lista.append(10)
        self.assertEqual(self.lista.find(lambda x: x == 10), 10)

    def test_filter(self):
        self.lista.append(1)
        self.lista.append(2)
        self.lista.append(3)
        result = self.lista.filter(lambda x: x > 1)
        self.assertEqual(result, [2, 3])


class TestHashTable(unittest.TestCase):
    """Pruebas para la tabla hash."""

    def setUp(self):
        self.tabla = HashTable()

    def test_put_and_get(self):
        self.tabla.put("clave", "valor")
        self.assertEqual(self.tabla.get("clave"), "valor")

    def test_get_non_existing(self):
        self.assertIsNone(self.tabla.get("inexistente"))

    def test_update_existing_key(self):
        self.tabla.put("k", "v1")
        self.tabla.put("k", "v2")
        self.assertEqual(self.tabla.get("k"), "v2")
        self.assertEqual(self.tabla.size(), 1)

    def test_remove(self):
        self.tabla.put("a", 1)
        self.assertTrue(self.tabla.remove("a"))
        self.assertIsNone(self.tabla.get("a"))
        self.assertEqual(self.tabla.size(), 0)

    def test_remove_non_existing(self):
        self.assertFalse(self.tabla.remove("nada"))

    def test_contains(self):
        self.tabla.put("existe", True)
        self.assertTrue(self.tabla.contains("existe"))
        self.assertFalse(self.tabla.contains("no_existe"))

    def test_keys_and_values(self):
        self.tabla.put("a", 1)
        self.tabla.put("b", 2)
        self.assertIn("a", self.tabla.keys())
        self.assertIn(2, self.tabla.values())


class TestQueue(unittest.TestCase):
    """Pruebas para la cola FIFO."""

    def setUp(self):
        self.cola = Queue()

    def test_enqueue_dequeue(self):
        self.cola.enqueue("primero")
        self.cola.enqueue("segundo")
        self.assertEqual(self.cola.dequeue(), "primero")

    def test_dequeue_empty(self):
        with self.assertRaises(IndexError):
            self.cola.dequeue()

    def test_peek(self):
        self.cola.enqueue("uno")
        self.assertEqual(self.cola.peek(), "uno")
        self.assertEqual(self.cola.size(), 1)

    def test_peek_empty(self):
        self.assertIsNone(self.cola.peek())

    def test_fifo_order(self):
        for i in range(5):
            self.cola.enqueue(i)
        result = [self.cola.dequeue() for _ in range(5)]
        self.assertEqual(result, [0, 1, 2, 3, 4])


class TestStack(unittest.TestCase):
    """Pruebas para la pila LIFO."""

    def setUp(self):
        self.pila = Stack()

    def test_push_pop(self):
        self.pila.push("a")
        self.pila.push("b")
        self.assertEqual(self.pila.pop(), "b")

    def test_pop_empty(self):
        with self.assertRaises(IndexError):
            self.pila.pop()

    def test_peek(self):
        self.pila.push(42)
        self.assertEqual(self.pila.peek(), 42)
        self.assertEqual(self.pila.size(), 1)

    def test_lifo_order(self):
        for i in range(3):
            self.pila.push(i)
        result = [self.pila.pop() for _ in range(3)]
        self.assertEqual(result, [2, 1, 0])


class TestSetRegistry(unittest.TestCase):
    """Pruebas para el conjunto de registros únicos."""

    def setUp(self):
        self.registro = SetRegistry()

    def test_add_unique(self):
        self.assertTrue(self.registro.add("a"))
        self.assertFalse(self.registro.add("a"))

    def test_remove(self):
        self.registro.add("x")
        self.assertTrue(self.registro.remove("x"))
        self.assertFalse(self.registro.contains("x"))

    def test_remove_non_existing(self):
        self.assertFalse(self.registro.remove("nada"))

    def test_contains(self):
        self.registro.add("dato")
        self.assertTrue(self.registro.contains("dato"))
        self.assertFalse(self.registro.contains("otro"))

    def test_size(self):
        self.registro.add("a")
        self.registro.add("b")
        self.registro.add("a")  # duplicado
        self.assertEqual(self.registro.size(), 2)


if __name__ == "__main__":
    unittest.main()
