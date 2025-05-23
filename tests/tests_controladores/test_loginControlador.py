import unittest
from mysql.connector.connection import MySQLConnection
from controladores.loginControlador import ControladorLogin

class TestControladorLogin(unittest.TestCase):
    def setUp(self):
        self.ctrl = ControladorLogin()

    def test_conexion_inicial_es_None(self):
        self.assertIsNone(self.ctrl.conexion)

    def test_conexion_base_datos(self):
        conexion = self.ctrl.conexion_base_datos('root', '', 'localhost', 'daw_prog')
        self.assertIsInstance(conexion, MySQLConnection)

    def test_conexion_base_datos_falla_base_datos_incorrecta(self, mock_mysql_connect):
        conexion = self.ctrl.conexion_base_datos('user', 'password', 'localhost', 'daw_prog')
        self.assertIsNone(conexion)
        self.assertIsNotNone(self.ctrl.ventanaError)


if __name__ == '__main__':
    unittest.main()
