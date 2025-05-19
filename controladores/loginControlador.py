from PySide6.QtWidgets import QMainWindow, QWidget, QTableWidgetItem

from controladores.principalControlador import ControladorPrincipal
from vistas.ui_login import Ui_loginVentana
from vistas.ui_error import Ui_Form

import mysql.connector
from mysql.connector import errorcode
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
        try:   
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
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                return 'Error de conexión con la base de datos. Inténtelo de nuevo.'
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                return f'No existe la base de datos "{BaseDatos.DATABASE}".'
            return err
