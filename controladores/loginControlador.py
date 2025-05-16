from PySide6.QtWidgets import QMainWindow, QWidget, QTableWidgetItem

from controladores.principalControlador import ControladorPrincipal
from vistas.ui_login import Ui_loginVentana

import mysql.connector
from mysql.connector.connection import MySQLConnection


class ControladorLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.conexion = None

        self.ui = Ui_loginVentana()
        self.ui.setupUi(self)

        self.ui.botonConectar.clicked.connect(self.conectar_BBDD)


    def conectar_BBDD(self):
        usuario = self.ui.inputUsuario.text()
        password = self.ui.inputPassword.text()
        direccion = self.ui.inputDireccion.text()
        bbdd = self.ui.inputBBDD.text()
        self.conexion = self.conexion_base_datos(usuario, password, direccion, bbdd)

        self.ventanaPrincipal = ControladorPrincipal(self.conexion)
        self.ventanaPrincipal.show()
        # self.conexion.close()
        self.close()

    
    def conexion_base_datos(self, usuario, contrasenia, direccion, bbdd):
        conexion: MySQLConnection = mysql.connector.connect(
            user=str(usuario),  
            password=str(contrasenia),
            host=str(direccion),  
            database=str(bbdd)  
        )
        # conexion: MySQLConnection = mysql.connector.connect(
        #     user='root',
        #     password='',
        #     host='localhost',
        #     database='daw_fct_departamentos'
        # )
        return conexion
