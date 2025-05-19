import unittest
from PySide6.QtWidgets import QWidget
from vistas.ui_error import Ui_Form

class TestUiError(unittest.TestCase):
    def setUp(self):
        self.widget = QWidget()
        self.ui = Ui_Form()

    def test_setupUi_crea_atributos(self):
        self.ui.setupUi(self.widget)
        self.assertTrue(hasattr(self.ui, 'icono'))
        self.assertTrue(hasattr(self.ui, 'textoError'))

if __name__ == '__main__':
    unittest.main()
