import unittest
from PySide6.QtWidgets import QMainWindow
from vistas.ui_login import Ui_loginVentana

class TestUiLogin(unittest.TestCase):
    def setUp(self):
        self.window = QMainWindow()
        self.ui = Ui_loginVentana()

    def test_setupUi_crea_campos(self):
        self.ui.setupUi(self.window)
        self.assertTrue(hasattr(self.ui, 'inputUsuario'))
        self.assertTrue(hasattr(self.ui, 'inputPassword'))
        self.assertTrue(hasattr(self.ui, 'botonConectar'))

if __name__ == '__main__':
    unittest.main()
