import unittest
from controladores.lib.horas_departamentos import HorasDepartamentos

class DummyCursor:
    def __init__(self):
        self.commands = []
    def execute(self, cmd):
        self.commands.append(cmd)

class TestHorasDepartamentos(unittest.TestCase):
    def test_actualizar_datos_retorna_nombre_y_ejecuta_INSERT(self):
        cursor = DummyCursor()
        datos = [(1, '09:00', '17:00')]
        resultado = HorasDepartamentos.actualizar_datos(cursor, datos)
        self.assertEqual(resultado, 'horas_departamentos')
        self.assertTrue(cursor.commands[0].startswith('INSERT'))

if __name__ == '__main__':
    unittest.main()
