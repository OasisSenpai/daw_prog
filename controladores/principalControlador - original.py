from PySide6.QtWidgets import QMainWindow, QWidget, QTableWidgetItem
from vistas.ui_principal import Ui_MainWindow

import mysql.connector
from mysql.connector.connection import MySQLConnection

from controladores.lib.cursos import Cursos
from controladores.lib.materias import Materias
from controladores.lib.departamentos import Departamentos


class ControladorPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.cursos = []
        self.materias = []
        self.departamentos = []
        self.especialidades = []
        self.especialidades = []
        self.optativas = []
        self.tipos = []
        self.tablaActual = ''

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.vistaTabla = self.ui.vistaTabla

        self.ui.actionCursos.triggered.connect(self.mostrar_cursos)
        self.ui.actionMaterias.triggered.connect(self.mostrar_materias)
        self.ui.actionDepartamentos.triggered.connect(self.mostrar_departamentos)

        self.ui.entryBuscar.textChanged.connect(self.filtrar_tabla)

        self.ui.botonAniadirCampo.clicked.connect(self.aniadir_fila)
        self.ui.botonELiminarCampo.clicked.connect(self.borrar_fila)
        self.ui.botonGuardar.clicked.connect(self.guardar_tabla_bbdd)


    def aniadir_fila(self):
        fila = self.vistaTabla.rowCount()
        self.vistaTabla.insertRow(fila)


    def borrar_fila(self):
        filas_seleccionadas = self.vistaTabla.selectionModel().selectedRows()
        if filas_seleccionadas:
            filas_seleccionadas.sort(reverse=True)
            for fila in filas_seleccionadas:
                self.vistaTabla.removeRow(fila.row())

    
    def conexion_base_datos(self):
        conexion: MySQLConnection = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database='daw_fct_departamentos'
        )
        return conexion


    def filtrar_tabla(self, texto):
        match self.tablaActual:
            case 'cursos':
                Cursos.mostrar_datos([curso for curso in self.cursos if texto.lower() in curso[1].lower()], self.ui, self.vistaTabla)
            case 'materias':
                Materias.mostrar_datos([materia for materia in self.materias if texto.lower() in materia[1].lower()], self.ui, self.vistaTabla)
            case 'departamento':
                Departamentos.mostrar_datos([departamento for departamento in self.departamento if texto.lower() in departamento[2].lower()], self.ui, self.vistaTabla)


    def guardar_tabla_bbdd(self):
        datosTabla = []
        num_filas = self.vistaTabla.rowCount()
        num_columnas = self.vistaTabla.columnCount()
        for fila in range(num_filas):
            fila_datos = []
            for columna in range(num_columnas):
                item = self.vistaTabla.item(fila, columna)
                if item is not None:
                    fila_datos.append(item.text())
                else:
                    fila_datos.append("")
            datosTabla.append(fila_datos)
        
        # print(datosTabla)

        conexion = self.conexion_base_datos()
        cursor = conexion.cursor()
        match self.tablaActual:
            case 'cursos':
                cursor.execute('SELECT id FROM cursos')
                ids_existentes = [row[0] for row in cursor.fetchall()]
                for fila in datosTabla:
                    if int(fila[0]) not in ids_existentes:
                        cursor.execute(f"INSERT INTO cursos (id, nombre, grupos, turnos) VALUES ({fila[0]}, '{fila[1]}', {fila[2]}, {fila[3]})")
            case 'materias':
                cursor.execute('SELECT id FROM materias')
                ids_existentes = [row[0] for row in cursor.fetchall()]
                for fila in datosTabla:
                    if int(fila[0]) not in ids_existentes:
                        cursor.execute(f"INSERT INTO materias (nombre, id_curso, grupo, horas_semanales, id_tipo, id_departamento, id_especialidad, id_optativa) VALUES ('{fila[1] if fila[1] != '' else 'NULL'}', {fila[2] if fila[2] != '' else 'NULL'}, '{fila[3] if fila[3] != '' else 'NULL'}', {fila[4] if fila[4] != '' else 'NULL'}, {fila[5] if fila[5] != '' else 'NULL'}, {fila[6] if fila[6] != '' else 'NULL'}, {fila[7] if fila[7] != '' else 'NULL'}, {fila[8] if fila[8] != '' else 'NULL'})")
        
        conexion.commit()
        cursor.close()
        conexion.close()


    def mostrar_cursos(self):
        self.cursos = Cursos.leer_datos_tabla(self.conexion_base_datos())
        self.tablaActual = Cursos.mostrar_datos(self.cursos, self.ui, self.vistaTabla)


    def mostrar_departamentos(self):
        self.departamentos = Departamentos.leer_datos_tabla(self.conexion_base_datos())
        self.tablaActual = Departamentos.mostrar_datos(self.departamentos, self.ui, self.vistaTabla)


    def mostrar_materias(self):
        self.materias = Materias.leer_datos_tabla(self.conexion_base_datos())
        self.tablaActual = Materias.mostrar_datos(self.materias, self.ui, self.vistaTabla)
