from PySide6.QtWidgets import QMainWindow, QWidget, QTableWidgetItem
from vistas.ui_error import Ui_errorVentana


class ControladorError(QMainWindow):
    def __init__(self, mensaje: str) -> None:
        super().__init__()

        self.ui = Ui_errorVentana()
        self.ui.setupUi(self)

        self.ui.textoError.setText(mensaje)
        
        self.show()
