from PySide6.QtWidgets import QMainWindow, QWidget, QTableWidgetItem
from vistas.ui_principal import Ui_MainWindow

import mysql.connector
from mysql.connector.connection import MySQLConnection

from typing import List

from controladores.lib.cursos import Cursos
from controladores.lib.departamentos import Departamentos
from controladores.lib.especialidades import Especialidades
from controladores.lib.horas_departamentos import HorasDepartamentos
from controladores.lib.materias import Materias
from controladores.lib.materias_vista import MateriasVista
from controladores.lib.optativas import Optativas
from controladores.lib.tipo import Tipos
from controladores.lib.turnos import Turnos


class ControladorPrincipal(QMainWindow):
    def __init__(self, conexion) -> None:
        super().__init__()
        self.conexion: MySQLConnection = conexion

        self.cursos: List[(str)] = []
        self.departamentos: List[(str)] = []
        self.especialidades: List[(str)] = []
        self.horasDepartamentos: List[(str)] = []
        self.materias: List[(str)] = []
        self.materiasVista: List[(str)] = []
        self.optativas: List[(str)] = []
        self.tipos: List[(str)] = []
        self.turnos: List[(str)] = []
        self.tablaActual: str = ''

        # Ventana gráfica:
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.vistaTabla = self.ui.vistaTabla

        # Selección de tabla:
        self.ui.actionCursos.triggered.connect(self.mostrar_cursos)
        self.ui.actionDepartamentos.triggered.connect(self.mostrar_departamentos)
        self.ui.actionEspecialidades.triggered.connect(self.mostrar_especialidades)
        self.ui.actionHorasDepartamentos.triggered.connect(self.mostrar_horas_departementos)
        self.ui.actionMaterias.triggered.connect(self.mostrar_materias)
        self.ui.actionMateriasVista.triggered.connect(self.mostrar_materias_vista)
        self.ui.actionOptativas.triggered.connect(self.mostrar_optativas)
        self.ui.actionTiposAsignatura.triggered.connect(self.mostrar_tipos)
        self.ui.actionTurnos.triggered.connect(self.mostrar_turnos)

        # Exportar tabla actual:
        self.ui.actionExportar_tabla.triggered.connect(self.exportar_tabla)

        # Filtro por nombre:
        self.ui.entryBuscar.textChanged.connect(self.filtrar_tabla)

        # Acciones en las tablas:
        self.ui.botonAniadirCampo.clicked.connect(self.aniadir_fila)
        self.ui.botonELiminarCampo.clicked.connect(self.borrar_fila)
        self.ui.botonGuardar.clicked.connect(self.guardar_tabla_bbdd)


    def aniadir_fila(self) -> None:
        fila = self.vistaTabla.rowCount()
        self.vistaTabla.insertRow(fila)
        self.vistaTabla.scrollToBottom()


    def borrar_fila(self) -> None:
        filas_seleccionadas = self.vistaTabla.selectionModel().selectedRows()
        if filas_seleccionadas:
            filas_seleccionadas.sort(reverse=True)
            for fila in filas_seleccionadas:
                self.vistaTabla.removeRow(fila.row())


    def exportar_tabla(self) -> None:
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


    def filtrar_tabla(self, texto) -> None:
        match self.tablaActual:
            case 'cursos':
                Cursos.mostrar_datos([curso for curso in self.cursos if texto.lower() in curso[1].lower()], self.ui, self.vistaTabla)
            case 'departamentos':
                Departamentos.mostrar_datos([departamento for departamento in self.departamentos if texto.lower() in departamento[2].lower()], self.ui, self.vistaTabla)
            case 'especialidades':
                Especialidades.mostrar_datos([especialidad for especialidad in self.especialidades if texto.lower() in especialidad[1].lower()], self.ui, self.vistaTabla)
            case 'horasDepartamentos':
                HorasDepartamentos.mostrar_datos([horas_departamento for horas_departamento in self.horasDepartamentos if texto.lower() in horas_departamento[0].lower()], self.ui, self.vistaTabla)
            case 'materias':
                Materias.mostrar_datos([materia for materia in self.materias if texto.lower() in materia[1].lower()], self.ui, self.vistaTabla)
            case 'materiasVista':
                MateriasVista.mostrar_datos([materia for materia in self.materiasVista if texto.lower() in materia[1].lower()], self.ui, self.vistaTabla)
            case 'optativas':
                Optativas.mostrar_datos([optativa for optativa in self.optativas if texto.lower() in optativa[1].lower()], self.ui, self.vistaTabla)
            case 'tipos':
                Tipos.mostrar_datos([tipo for tipo in self.tipos if texto.lower() in tipo[1].lower()], self.ui, self.vistaTabla)
            case 'turnos':
                Turnos.mostrar_datos([turno for turno in self.turnos if texto.lower() in turno[1].lower()], self.ui, self.vistaTabla)


    def guardar_tabla_bbdd(self) -> None:
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
            case 'optativas':
                Optativas.actualizar_datos(cursor, datosTabla)
            case 'tipo_asignatura':
                Tipos.actualizar_datos(cursor, datosTabla)
            case 'turnos':
                Turnos.actualizar_datos(cursor, datosTabla)
        
        conexion.commit()
        cursor.close()


    def mostrar_cursos(self) -> None:
        self.cursos = Cursos.leer_datos_tabla(self.conexion)
        self.tablaActual = Cursos.mostrar_datos(self.cursos, self.ui, self.vistaTabla)


    def mostrar_departamentos(self) -> None:
        self.departamentos = Departamentos.leer_datos_tabla(self.conexion)
        self.tablaActual = Departamentos.mostrar_datos(self.departamentos, self.ui, self.vistaTabla)


    def mostrar_especialidades(self) -> None:
        self.especialidades = Especialidades.leer_datos_tabla(self.conexion)
        self.tablaActual = Especialidades.mostrar_datos(self.especialidades, self.ui, self.vistaTabla)


    def mostrar_horas_departementos(self) -> None:
        self.horasDepartamentos = HorasDepartamentos.leer_datos_tabla(self.conexion)
        self.tablaActual = HorasDepartamentos.mostrar_datos(self.horasDepartamentos, self.ui, self.vistaTabla, self.conexion)


    def mostrar_materias(self) -> None:
        self.materias = Materias.leer_datos_tabla(self.conexion)
        self.tablaActual = Materias.mostrar_datos(self.materias, self.ui, self.vistaTabla)


    def mostrar_materias_vista(self) -> None:
        self.materiasVista = MateriasVista.leer_datos_tabla(self.conexion)
        self.tablaActual = MateriasVista.mostrar_datos(self.materiasVista, self.ui, self.vistaTabla)


    def mostrar_optativas(self) -> None:
        self.optativas = Optativas.leer_datos_tabla(self.conexion)
        self.tablaActual = Optativas.mostrar_datos(self.optativas, self.ui, self.vistaTabla)


    def mostrar_tipos(self) -> None:
        self.tipos = Tipos.leer_datos_tabla(self.conexion)
        self.tablaActual = Tipos.mostrar_datos(self.tipos, self.ui, self.vistaTabla)


    def mostrar_turnos(self) -> None:
        self.turnos = Turnos.leer_datos_tabla(self.conexion)
        self.tablaActual = Turnos.mostrar_datos(self.turnos, self.ui, self.vistaTabla)
