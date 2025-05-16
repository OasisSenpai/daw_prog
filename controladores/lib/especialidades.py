from PySide6.QtWidgets import QTableWidgetItem

import mysql.connector


class Especialidades:
    @staticmethod
    def actualizar_datos(cursor, datosTabla):
        # Actualizar o insertar filas.
        for fila in datosTabla:
            sentenciaInsert = (f"INSERT INTO especialidades (id, nombre)\
                VALUES ({fila[0]}, '{fila[1]}')")
            sentenciaUpdate = (f"UPDATE especialidades SET nombre = '{fila[1]}' WHERE id = {fila[0]}")
            try:
                cursor.execute(sentenciaInsert)
            except mysql.connector.Error as error:
                if error.errno == 1062:  # errorcode.ER_DUP_ENTRY  # Duplicate entry error
                    cursor.execute(sentenciaUpdate)
                else:
                    print(error)

        # Eliminar filas que no están en la tabla.
        sentenciaSelect = (f"SELECT * FROM especialidades")
        cursor.execute(sentenciaSelect)
        for fila in cursor.fetchall():
            fila = [str(elemento) for elemento in fila]
            if fila not in datosTabla:
                cursor.execute(f"DELETE FROM especialidades WHERE id = {fila[0]}")


    @staticmethod
    def leer_datos_tabla(conexion):
        especialidades = []
        cursor = conexion.cursor()
        sql_lectura_datos: str = 'SELECT * FROM especialidades'
        cursor.execute(sql_lectura_datos)
        for registro in cursor.fetchall():
            especialidades.append(registro)
        cursor.close()
        # conexion.close()
        return especialidades


    @staticmethod
    def mostrar_datos(especialidades, ui, vistaTabla):
        vistaTabla.setRowCount(0)
        vistaTabla.setColumnCount(2)
        vistaTabla.setHorizontalHeaderLabels(["id", "nombre"])

        for departamento in especialidades:
            fila = vistaTabla.rowCount()
            vistaTabla.insertRow(fila)
            vistaTabla.setItem(fila, 0, QTableWidgetItem(str(departamento[0])))
            vistaTabla.setItem(fila, 1, QTableWidgetItem(str(departamento[1])))

        vistaTabla.resizeColumnsToContents()
        ui.nombreTabla.setText('Especialidades')
        return 'especialidades'
