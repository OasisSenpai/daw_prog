import unittest
from controladores.lib.optativas import Optativas

class DummyCursor:
    def __init__(self):
        self.commands = []
    def execute(self, cmd):
        self.commands.append(cmd)

class TestOptativas(unittest.TestCase):
    def test_actualizar_datos_retorna_nombre_y_ejecuta_INSERT(self):
        cursor = DummyCursor()
        datos = [(1, 'OptativaTest')]
        resultado = Optativas.actualizar_datos(cursor, datos)
        self.assertEqual(resultado, 'optativas')
        self.assertTrue(cursor.commands[0].startswith('INSERT'))

if __name__ == '__main__':
    unittest.main()
