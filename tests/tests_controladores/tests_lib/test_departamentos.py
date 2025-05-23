import unittest
from controladores.lib.departamentos import Departamentos

class DummyCursor:
    def __init__(self):
        self.commands = []
    def execute(self, cmd):
        self.commands.append(cmd)

class TestDepartamentos(unittest.TestCase):
    def test_actualizar_datos_retorna_nombre_y_ejecuta_INSERT(self):
        cursor = DummyCursor()
        datos = [(1, 'D01', 'DeptoTest')]
        resultado = Departamentos.actualizar_datos(cursor, datos)
        self.assertEqual(resultado, 'departamentos')
        self.assertTrue('INSERT INTO departamentos' in cursor.commands[0])

if __name__ == '__main__':
    unittest.main()
