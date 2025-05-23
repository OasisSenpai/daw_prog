import unittest
from controladores.principalControlador import ControladorPrincipal

import mysql.connector
from mysql.connector.connection import MySQLConnection


class TestControladorPrincipal(unittest.TestCase):
    def setUp(self):
        conexion: MySQLConnection = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database='daw_prog'
        )
        self.ctrl = ControladorPrincipal(conexion)

    def test_atributos_iniciales(self):
        self.assertTrue(hasattr(self.ctrl, 'conexion'))
        self.assertTrue(hasattr(self.ctrl, 'ui'))
        self.assertTrue(hasattr(self.ctrl, 'vistaTabla'))

    def test_mostrar_cursos(self):
        self.ctrl.mostrar_cursos()
        self.assertEqual(self.ctrl.tablaActual, 'cursos')

    def test_mostrar_departamentos(self):
        self.ctrl.mostrar_departamentos()
        self.assertEqual(self.ctrl.tablaActual, 'departamentos')

    def test_mostrar_especialidades(self):
        self.ctrl.mostrar_especialidades()
        self.assertEqual(self.ctrl.tablaActual, 'especialidades')

    def test_mostrar_horas_departementos(self):
        self.ctrl.mostrar_horas_departementos()
        self.assertEqual(self.ctrl.tablaActual, 'horasDepartamentos')

    def test_mostrar_materias(self):
        self.ctrl.mostrar_materias()
        self.assertEqual(self.ctrl.tablaActual, 'materias')

    def test_mostrar_materias_vista(self):
        self.ctrl.mostrar_materias_vista()
        self.assertEqual(self.ctrl.tablaActual, 'materiasVista')

    def test_mostrar_optativas(self):
        self.ctrl.mostrar_optativas()
        self.assertEqual(self.ctrl.tablaActual, 'optativas')

    def test_mostrar_tipos(self):
        self.ctrl.mostrar_tipos()
        self.assertEqual(self.ctrl.tablaActual, 'tipo_asignatura')

    def test_mostrar_turnos(self):
        self.ctrl.mostrar_turnos()
        self.assertEqual(self.ctrl.tablaActual, 'turnos')


    # def test_mostrar_especialidades_asigna_tablaActual(self):
    #     datos = [('1', 'Especialidad X')]

    #     Especialidades.leer_datos_tabla = staticmethod(lambda c: datos)
    #     Especialidades.mostrar_datos   = staticmethod(lambda d, ui, tabla: 'especialidades')
    #     # Ejecutamos
    #     self.ctrl.conexion = object()
    #     self.ctrl.mostrar_especialidades()
    #     # assertEqual
    #     self.assertEqual(self.ctrl.tablaActual, 'especialidades')

if __name__ == '__main__':
    unittest.main()
