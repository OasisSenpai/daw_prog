import unittest
from controladores.lib.materias_vista import MateriasVista

class DummyCursor:
    def __init__(self):
        self.commands = []
    def execute(self, cmd):
        self.commands.append(cmd)

class TestMateriasVista(unittest.TestCase):
    def test_actualizar_datos_retorna_nombre_y_ejecuta_INSERT(self):
        cursor = DummyCursor()
        datos = [(1, 'MatVista', 4)]
        resultado = MateriasVista.actualizar_datos(cursor, datos)
        self.assertEqual(resultado, 'materias_vista')
        self.assertTrue('INSERT' in cursor.commands[0])

if __name__ == '__main__':
    unittest.main()
