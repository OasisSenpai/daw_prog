import unittest
from controladores.lib.cursos import Cursos

class DummyCursor:
    def __init__(self):
        self.commands = []
    def execute(self, cmd):
        self.commands.append(cmd)

class TestCursos(unittest.TestCase):
    def test_actualizar_datos_retorna_nombre_y_ejecuta_INSERT(self):
        cursor = DummyCursor()
        datos = [(1, 'CursoTest', 2, 3)]
        resultado = Cursos.actualizar_datos(cursor, datos)
        # assertEqual
        self.assertEqual(resultado, 'cursos')
        # assertTrue
        self.assertTrue(cursor.commands[0].startswith('INSERT'))

if __name__ == '__main__':
    unittest.main()
