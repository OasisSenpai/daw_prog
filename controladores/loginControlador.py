from PySide6.QtWidgets import QMainWindow, QWidget, QTableWidgetItem

from controladores.principalControlador import ControladorPrincipal
from vistas.ui_login import Ui_loginVentana

import mysql.connector
from mysql.connector.connection import MySQLConnection


class ControladorLogin(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.conexion = None

        self.ui = Ui_loginVentana()
        self.ui.setupUi(self)

        self.ui.botonConectar.clicked.connect(self.conectar_BBDD)


    def conectar_BBDD(self) -> None:
        usuario: str = str(self.ui.inputUsuario.text())
        password: str = str(self.ui.inputPassword.text())
        direccion: str = str(self.ui.inputDireccion.text())
        bbdd: str = str(self.ui.inputBBDD.text())
        self.conexion: MySQLConnection = self.conexion_base_datos(usuario, password, direccion, bbdd)

        self.ventanaPrincipal = ControladorPrincipal(self.conexion)
        self.ventanaPrincipal.show()
        # self.conexion.close()
        self.close()

    
    def conexion_base_datos(self, usuario: str, contrasenia: str, direccion: str, bbdd: str) -> MySQLConnection:
        # conexion: MySQLConnection = mysql.connector.connect(
        #     user=usuario,  
        #     password=contrasenia,
        #     host=direccion,  
        #     database=bbdd  
        # )
        conexion: MySQLConnection = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database='daw_prog'
        )
        return conexion
