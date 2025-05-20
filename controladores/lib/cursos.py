from PySide6.QtWidgets import QTableWidgetItem

import mysql.connector


class Cursos:
    @staticmethod
    def actualizar_datos(cursor, datosTabla):
        # Actualizar o insertar fila.
        for fila in datosTabla:
            sentenciaInsert = (f"INSERT INTO cursos (id, nombre, grupos, turnos)\
                VALUES ({fila[0]}, '{fila[1]}', {fila[2]}, {fila[3]})")
            sentenciaUpdate = (f"UPDATE cursos SET nombre = '{fila[1]}', grupos = {fila[2]}, turnos = {fila[3]} WHERE id = {fila[0]}")
            try:
                cursor.execute(sentenciaInsert)
            except mysql.connector.Error as error:
                if error.errno == 1062:  # errorcode.ER_DUP_ENTRY  # Duplicate entry error
                    cursor.execute(sentenciaUpdate)
                else:
                    print(error)

        # Eliminar filas que no están en la tabla.
        sentenciaSelect = (f"SELECT * FROM cursos")
        cursor.execute(sentenciaSelect)
        for fila in cursor.fetchall():
            fila = [str(elemento) for elemento in fila]
            if fila not in datosTabla:
                cursor.execute(f"DELETE FROM cursos WHERE id = {fila[0]}")


    @staticmethod
    def leer_datos_tabla(conexion):
        cursos = []
        cursor = conexion.cursor()
        sql_lectura_datos: str = 'SELECT * FROM cursos'
        cursor.execute(sql_lectura_datos)
        for registro in cursor.fetchall():
            cursos.append(registro)
        cursor.close()
        # conexion.close()
        return cursos


    @staticmethod
    def mostrar_datos(cursos, ui, vistaTabla):
        vistaTabla.setRowCount(0)
        vistaTabla.setColumnCount(4)
        vistaTabla.setHorizontalHeaderLabels(["id", "nombre", "grupos", "turnos"])

        for curso in cursos:
            fila = vistaTabla.rowCount()
            vistaTabla.insertRow(fila)
            vistaTabla.setItem(fila, 0, QTableWidgetItem(str(curso[0]).replace('\n', '')))
            vistaTabla.setItem(fila, 1, QTableWidgetItem(str(curso[1]).replace('\n', '')))
            vistaTabla.setItem(fila, 2, QTableWidgetItem(str(curso[2]).replace('\n', '')))
            vistaTabla.setItem(fila, 3, QTableWidgetItem(str(curso[3]).replace('\n', '')))

        vistaTabla.resizeColumnsToContents()
        ui.nombreTabla.setText('Cursos')
        return 'cursos'


if __name__ == '__main__':
    pass
