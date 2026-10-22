import unittest
from tasks import agregar_tarea, completar_tarea, pendientes

class TestTasks(unittest.TestCase):
    def test_agregar_tarea(self):
        tareas = []
        tarea = agregar_tarea(tareas, "Leer documentación")
        self.assertEqual(tarea["titulo"], "Leer documentación")
        self.assertEqual(tarea["categoria"], "General")
        self.assertFalse(tarea["completada"])

    def test_agregar_tarea_con_categoria(self):
        tareas = []
        tarea = agregar_tarea(tareas, "Leer documentación", "  Estudio  ")
        self.assertEqual(tarea["categoria"], "Estudio")

    def test_agregar_tarea_con_categoria_vacia(self):
        with self.assertRaises(ValueError):
            agregar_tarea([], "Leer documentación", "   ")

    def test_completar_tarea(self):
        tareas = []
        agregar_tarea(tareas, "Practicar")
        completar_tarea(tareas, 1)
        self.assertEqual(pendientes(tareas), [])

    def test_pendientes_por_categoria_sin_distinguir_mayusculas(self):
        tareas = []
        tarea_estudio = agregar_tarea(tareas, "Leer", "Estudio")
        agregar_tarea(tareas, "Trabajar", "Trabajo")

        self.assertEqual(pendientes(tareas, "eSTUDIO"), [tarea_estudio])

    def test_pendientes_por_categoria_inexistente(self):
        tareas = []
        agregar_tarea(tareas, "Leer", "Estudio")

        self.assertEqual(pendientes(tareas, "Inexistente"), [])

if __name__ == "__main__":
    unittest.main()
