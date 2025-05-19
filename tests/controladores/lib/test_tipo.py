import unittest
from controladores.lib.tipo import Tipos

class DummyCursor:
    def __init__(self):
        self.commands = []
    def execute(self, cmd):
        self.commands.append(cmd)

class TestTipos(unittest.TestCase):
    def test_actualizar_datos_retorna_nombre_y_ejecuta_INSERT(self):
        cursor = DummyCursor()
        datos = [(1, 'TipoTest')]
        resultado = Tipos.actualizar_datos(cursor, datos)
        self.assertEqual(resultado, 'tipo')
        self.assertIn('INSERT INTO tipo', cursor.commands[0])

if __name__ == '__main__':
    unittest.main()
