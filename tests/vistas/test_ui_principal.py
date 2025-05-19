import unittest
from PySide6.QtWidgets import QMainWindow
from vistas.ui_principal import Ui_MainWindow

class TestUiPrincipal(unittest.TestCase):
    def setUp(self):
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()

    def test_setupUi_crea_paneles(self):
        self.ui.setupUi(self.window)
        # p.ej. compruebo que exista el widget de tabla
        self.assertTrue(hasattr(self.ui, 'tablaDepartamentos'))
        self.assertTrue(hasattr(self.ui, 'actionSalir'))

if __name__ == '__main__':
    unittest.main()
