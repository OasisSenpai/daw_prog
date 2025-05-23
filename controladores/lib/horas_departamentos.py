from PySide6.QtWidgets import QTableWidgetItem

import mysql.connector


class HorasDepartamentos:
    @staticmethod
    def leer_datos_tabla(conexion):
        materias = []
        cursor = conexion.cursor()
        sql_lectura_datos: str = 'SELECT * FROM vista_horas_departamentos'
        cursor.execute(sql_lectura_datos)
        for registro in cursor.fetchall():
            materias.append(registro)
        cursor.close()
        # conexion.close()
        return materias


    @staticmethod
    def mostrar_datos(materias, ui, vistaTabla, conexion):
        cursor = conexion.cursor()
        cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'vista_horas_departamentos';")
        nombres_columnas = [columna[0] for columna in cursor.fetchall()]
        vistaTabla.setRowCount(0)
        vistaTabla.setColumnCount(31)
        vistaTabla.setHorizontalHeaderLabels(nombres_columnas)

        # print(nombres_columnas)

        for materia in materias:
            fila = vistaTabla.rowCount()
            vistaTabla.insertRow(fila)
            vistaTabla.setItem(fila, 0, QTableWidgetItem(str(materia[0]).replace('\n', '')))
            vistaTabla.setItem(fila, 1, QTableWidgetItem(str(materia[1]).replace('\n', '')))
            vistaTabla.setItem(fila, 2, QTableWidgetItem(str(materia[2]).replace('\n', '')))
            vistaTabla.setItem(fila, 3, QTableWidgetItem(str(materia[3]).replace('\n', '')))
            vistaTabla.setItem(fila, 4, QTableWidgetItem(str(materia[4]).replace('\n', '')))
            vistaTabla.setItem(fila, 5, QTableWidgetItem(str(materia[5]).replace('\n', '')))
            vistaTabla.setItem(fila, 6, QTableWidgetItem(str(materia[6]).replace('\n', '')))
            vistaTabla.setItem(fila, 7, QTableWidgetItem(str(materia[7]).replace('\n', '')))
            vistaTabla.setItem(fila, 8, QTableWidgetItem(str(materia[8]).replace('\n', '')))
            vistaTabla.setItem(fila, 9, QTableWidgetItem(str(materia[9]).replace('\n', '')))
            vistaTabla.setItem(fila, 10, QTableWidgetItem(str(materia[10]).replace('\n', '')))
            vistaTabla.setItem(fila, 11, QTableWidgetItem(str(materia[11]).replace('\n', '')))
            vistaTabla.setItem(fila, 12, QTableWidgetItem(str(materia[12]).replace('\n', '')))
            vistaTabla.setItem(fila, 13, QTableWidgetItem(str(materia[13]).replace('\n', '')))
            vistaTabla.setItem(fila, 14, QTableWidgetItem(str(materia[14]).replace('\n', '')))
            vistaTabla.setItem(fila, 15, QTableWidgetItem(str(materia[15]).replace('\n', '')))
            vistaTabla.setItem(fila, 16, QTableWidgetItem(str(materia[16]).replace('\n', '')))
            vistaTabla.setItem(fila, 17, QTableWidgetItem(str(materia[17]).replace('\n', '')))
            vistaTabla.setItem(fila, 18, QTableWidgetItem(str(materia[18]).replace('\n', '')))
            vistaTabla.setItem(fila, 19, QTableWidgetItem(str(materia[19]).replace('\n', '')))
            vistaTabla.setItem(fila, 20, QTableWidgetItem(str(materia[20]).replace('\n', '')))
            vistaTabla.setItem(fila, 21, QTableWidgetItem(str(materia[21]).replace('\n', '')))
            vistaTabla.setItem(fila, 22, QTableWidgetItem(str(materia[22]).replace('\n', '')))
            vistaTabla.setItem(fila, 23, QTableWidgetItem(str(materia[23]).replace('\n', '')))
            vistaTabla.setItem(fila, 24, QTableWidgetItem(str(materia[24]).replace('\n', '')))
            vistaTabla.setItem(fila, 25, QTableWidgetItem(str(materia[25]).replace('\n', '')))
            vistaTabla.setItem(fila, 26, QTableWidgetItem(str(materia[26]).replace('\n', '')))
            vistaTabla.setItem(fila, 27, QTableWidgetItem(str(materia[27]).replace('\n', '')))
            vistaTabla.setItem(fila, 28, QTableWidgetItem(str(materia[28]).replace('\n', '')))
            vistaTabla.setItem(fila, 29, QTableWidgetItem(str(materia[29]).replace('\n', '')))
            vistaTabla.setItem(fila, 30, QTableWidgetItem(str(materia[30]).replace('\n', '')))

        vistaTabla.resizeColumnsToContents()
        ui.nombreTabla.setText('Horas departamentos')
        return 'horasDepartamentos'
