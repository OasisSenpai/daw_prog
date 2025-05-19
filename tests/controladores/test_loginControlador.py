import unittest
from mysql.connector.connection import MySQLConnection
from controladores.loginControlador import ControladorLogin

class TestControladorLogin(unittest.TestCase):
    def setUp(self):
        self.ctrl = ControladorLogin()

    def test_conexion_inicial_es_None(self):
        # assertIsNone
        self.assertIsNone(self.ctrl.conexion)

    def test_conexion_base_datos_devuelve_MySQLConnection(self):
        conn = self.ctrl.conexion_base_datos('usuario', 'pass', 'host', 'db')
        # assertIsInstance
        self.assertIsInstance(conn, MySQLConnection)

if __name__ == '__main__':
    unittest.main()
