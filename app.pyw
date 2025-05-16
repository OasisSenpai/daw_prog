import sys
from PySide6.QtWidgets import QApplication, QMainWindow

# from controladores.principalControlador import ControladorPrincipal
from controladores.loginControlador import ControladorLogin


class App(QMainWindow):
    def __init__(self):
        self.app = QApplication(sys.argv)
        # self.app.setStyle("fusion")
        self.ventanaLogin = ControladorLogin()
        # self.ventanaPrincipal = ControladorPrincipal()

    def run(self):
        self.ventanaLogin.show()
        # self.ventanaPrincipal.show()
        sys.exit(self.app.exec())



if __name__ == "__main__":
    app = App()
    app.run()
