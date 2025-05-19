import unittest
from controladores.lib.especialidades import Especialidades

class DummyCursor:
    def __init__(self):
        self.commands = []
    def execute(self, cmd):
        self.commands.append(cmd)

class TestEspecialidades(unittest.TestCase):
    def test_actualizar_datos_retorna_nombre_y_ejecuta_INSERT(self):
        cursor = DummyCursor()
        datos = [(1, 'EspTest')]
        resultado = Especialidades.actualizar_datos(cursor, datos)
        self.assertEqual(resultado, 'especialidades')
        self.assertIn('INSERT INTO especialidades', cursor.commands[0])

if __name__ == '__main__':
    unittest.main()
