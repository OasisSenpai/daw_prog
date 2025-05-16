from PySide6.QtWidgets import QTableWidgetItem

import mysql.connector


class Materias:
    @staticmethod
    def actualizar_datos(cursor, datosTabla):
        # Actualizar o insertar fila.
        pass


    @staticmethod
    def leer_datos_tabla(conexion):
        materias = []
        cursor = conexion.cursor()
        sql_lectura_datos: str = 'SELECT * FROM vista_materias_cursos'
        cursor.execute(sql_lectura_datos)
        for registro in cursor.fetchall():
            materias.append(registro)
        cursor.close()
        # conexion.close()
        return materias


    @staticmethod
    def mostrar_datos(materias, ui, vistaTabla):
        vistaTabla.setRowCount(0)
        vistaTabla.setColumnCount(9)
        vistaTabla.setHorizontalHeaderLabels(["id", "nombre", "id_curso", "grupo", "horas_semanales", "id_tipo", "id_departamento", "id_especialidad", "id_optativa"])

        for materia in materias:
            fila = vistaTabla.rowCount()
            vistaTabla.insertRow(fila)
            vistaTabla.setItem(fila, 0, QTableWidgetItem(str(materia[0])))
            vistaTabla.setItem(fila, 1, QTableWidgetItem(str(materia[1])))
            vistaTabla.setItem(fila, 2, QTableWidgetItem(str(materia[2])))
            vistaTabla.setItem(fila, 3, QTableWidgetItem(str(materia[3])))
            vistaTabla.setItem(fila, 4, QTableWidgetItem(str(materia[4])))
            vistaTabla.setItem(fila, 5, QTableWidgetItem(str(materia[5])))
            vistaTabla.setItem(fila, 6, QTableWidgetItem(str(materia[6])))
            vistaTabla.setItem(fila, 7, QTableWidgetItem(str(materia[7])))
            vistaTabla.setItem(fila, 8, QTableWidgetItem(str(materia[8])))

        vistaTabla.resizeColumnsToContents()
        ui.nombreTabla.setText('Materias')
        return 'materias'
