import unittest
import sys
from PySide6.QtWidgets import QApplication
from app import App
from controladores.loginControlador import ControladorLogin

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app_inst = App()

    def test_app_es_QApplication(self):
        # assertIsInstance
        self.assertIsInstance(self.app_inst.app, QApplication)

    def test_ventanaLogin_es_ControladorLogin(self):
        # assertIsInstance
        self.assertIsInstance(self.app_inst.ventanaLogin, ControladorLogin)

    def test_run_lanza_SystemExit(self):
        # assertRaises
        with self.assertRaises(SystemExit):
            # .run() hará sys.exit()
            self.app_inst.run()

if __name__ == '__main__':
    unittest.main()
