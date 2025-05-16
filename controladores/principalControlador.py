from PySide6.QtWidgets import QMainWindow, QWidget, QTableWidgetItem
from vistas.ui_principal import Ui_MainWindow

import mysql.connector
from mysql.connector.connection import MySQLConnection

from controladores.lib.cursos import Cursos
from controladores.lib.departamentos import Departamentos
from controladores.lib.especialidades import Especialidades
from controladores.lib.horas_departamentos import HorasDepartamentos
from controladores.lib.materias import Materias
from controladores.lib.optativas import Optativas
from controladores.lib.tipo import Tipos
from controladores.lib.turnos import Turnos


class ControladorPrincipal(QMainWindow):
    def __init__(self, conexion):
        super().__init__()
        self.conexion = conexion

        self.cursos = []
        self.departamentos = []
        self.especialidades = []
        self.horas_departamentos = []
        self.materias = []
        self.optativas = []
        self.tipos = []
        self.turnos = []
        self.tablaActual = ''

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.vistaTabla = self.ui.vistaTabla

        self.ui.actionCursos.triggered.connect(self.mostrar_cursos)
        self.ui.actionDepartamentos.triggered.connect(self.mostrar_departamentos)
        self.ui.actionEspecialidades.triggered.connect(self.mostrar_especialidades)
        self.ui.actionHorasDepartamentos.triggered.connect(self.mostrar_horas_departementos)
        self.ui.actionMaterias.triggered.connect(self.mostrar_materias)
        self.ui.actionOptativas.triggered.connect(self.mostrar_optativas)
        self.ui.actionTipos_de_asignatura.triggered.connect(self.mostrar_tipos)
        self.ui.actionTurnos.triggered.connect(self.mostrar_turnos)

        self.ui.actionExportar_tabla.triggered.connect(self.exportar_tabla)

        self.ui.entryBuscar.textChanged.connect(self.filtrar_tabla)

        self.ui.botonAniadirCampo.clicked.connect(self.aniadir_fila)
        self.ui.botonELiminarCampo.clicked.connect(self.borrar_fila)
        self.ui.botonGuardar.clicked.connect(self.guardar_tabla_bbdd)


    def aniadir_fila(self):
        fila = self.vistaTabla.rowCount()
        self.vistaTabla.insertRow(fila)
        self.vistaTabla.scrollToBottom()


    def borrar_fila(self):
        filas_seleccionadas = self.vistaTabla.selectionModel().selectedRows()
        if filas_seleccionadas:
            filas_seleccionadas.sort(reverse=True)
            for fila in filas_seleccionadas:
                self.vistaTabla.removeRow(fila.row())

    
    # def conexion_base_datos(self):
    #     conexion: MySQLConnection = mysql.connector.connect(
    #         user='root',
    #         password='',
    #         host='localhost',
    #         database='daw_fct_pruebas'
    #     )
    #     return conexion


    def exportar_tabla(self):
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
        with open(f'{self.tablaActual}.csv', 'w', encoding='utf-8') as archivo:
            for fila in datosTabla:
                archivo.write(f'{fila}\n')


    def filtrar_tabla(self, texto):
        match self.tablaActual:
            case 'cursos':
                Cursos.mostrar_datos([curso for curso in self.cursos if texto.lower() in curso[1].lower()], self.ui, self.vistaTabla)
            case 'departamentos':
                Departamentos.mostrar_datos([departamento for departamento in self.departamentos if texto.lower() in departamento[2].lower()], self.ui, self.vistaTabla)
            case 'especialidades':
                Especialidades.mostrar_datos([especialidad for especialidad in self.especialidades if texto.lower() in especialidad[1].lower()], self.ui, self.vistaTabla)
            case 'horas_departamentos':
                HorasDepartamentos.mostrar_datos([horas_departamento for horas_departamento in self.horas_departamentos if texto.lower() in horas_departamento[0].lower()], self.ui, self.vistaTabla)
            case 'materias':
                Materias.mostrar_datos([materia for materia in self.materias if texto.lower() in materia[1].lower()], self.ui, self.vistaTabla)
            case 'optativas':
                Optativas.mostrar_datos([optativa for optativa in self.optativas if texto.lower() in optativa[1].lower()], self.ui, self.vistaTabla)
            case 'tipos':
                Tipos.mostrar_datos([tipo for tipo in self.tipos if texto.lower() in tipo[1].lower()], self.ui, self.vistaTabla)
            case 'turnos':
                Turnos.mostrar_datos([turno for turno in self.turnos if texto.lower() in turno[1].lower()], self.ui, self.vistaTabla)


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

        conexion = self.conexion
        cursor = conexion.cursor()
        match self.tablaActual:
            case 'cursos':
                Cursos.actualizar_datos(cursor, datosTabla)
            case 'materias':
                Materias.actualizar_datos(cursor, datosTabla)
            case 'departamentos':
                Departamentos.actualizar_datos(cursor, datosTabla)
            case 'especialidades':
                Especialidades.actualizar_datos(cursor, datosTabla)
            case 'horas_departamentos':
                HorasDepartamentos.actualizar_datos(cursor, datosTabla)
            case 'optativas':
                Optativas.actualizar_datos(cursor, datosTabla)
            case 'tipo_asignatura':
                Tipos.actualizar_datos(cursor, datosTabla)
            case 'turnos':
                Turnos.actualizar_datos(cursor, datosTabla)
        
        conexion.commit()
        cursor.close()
        # conexion.close()


    def mostrar_cursos(self):
        self.cursos = Cursos.leer_datos_tabla(self.conexion)
        self.tablaActual = Cursos.mostrar_datos(self.cursos, self.ui, self.vistaTabla)


    def mostrar_departamentos(self):
        self.departamentos = Departamentos.leer_datos_tabla(self.conexion)
        self.tablaActual = Departamentos.mostrar_datos(self.departamentos, self.ui, self.vistaTabla)


    def mostrar_especialidades(self):
        self.especialidades = Especialidades.leer_datos_tabla(self.conexion)
        self.tablaActual = Especialidades.mostrar_datos(self.especialidades, self.ui, self.vistaTabla)


    def mostrar_horas_departementos(self):
        self.horas_departamentos = HorasDepartamentos.leer_datos_tabla(self.conexion)
        self.tablaActual = HorasDepartamentos.mostrar_datos(self.horas_departamentos, self.ui, self.vistaTabla, self.conexion)


    def mostrar_materias(self):
        self.materias = Materias.leer_datos_tabla(self.conexion)
        self.tablaActual = Materias.mostrar_datos(self.materias, self.ui, self.vistaTabla)


    def mostrar_optativas(self):
        self.optativas = Optativas.leer_datos_tabla(self.conexion)
        self.tablaActual = Optativas.mostrar_datos(self.optativas, self.ui, self.vistaTabla)


    def mostrar_tipos(self):
        self.tipos = Tipos.leer_datos_tabla(self.conexion)
        self.tablaActual = Tipos.mostrar_datos(self.tipos, self.ui, self.vistaTabla)


    def mostrar_turnos(self):
        self.turnos = Turnos.leer_datos_tabla(self.conexion)
        self.tablaActual = Turnos.mostrar_datos(self.turnos, self.ui, self.vistaTabla)
