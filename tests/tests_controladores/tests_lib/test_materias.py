import unittest
from controladores.lib.materias import Materias

class DummyCursor:
    def __init__(self):
        self.commands = []
    def execute(self, cmd):
        self.commands.append(cmd)

class TestMaterias(unittest.TestCase):
    def test_actualizar_datos_retorna_nombre_y_ejecuta_INSERT(self):
        cursor = DummyCursor()
        datos = [(1, 'MateriaTest', 3)]
        resultado = Materias.actualizar_datos(cursor, datos)
        self.assertEqual(resultado, 'materias')
        self.assertIn('INSERT INTO materias', cursor.commands[0])

if __name__ == '__main__':
    unittest.main()
