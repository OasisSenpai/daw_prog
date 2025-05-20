from PySide6.QtWidgets import QTableWidgetItem

import mysql.connector


class Tipos:
    @staticmethod
    def actualizar_datos(cursor, datosTabla):
        # Actualizar o insertar filas.
        for fila in datosTabla:
            sentenciaInsert = (f"INSERT INTO tipo_asignatura (id, nombre, clave_tipo, añadir, factor)\
                VALUES ({fila[0]}, '{fila[1]}', '{fila[2]}', {fila[3]}, {fila[4]})")
            sentenciaUpdate = (f"UPDATE tipo_asignatura SET nombre = '{fila[1]}', clave_tipo = '{fila[2]}', añadir = {fila[3]}, factor = {fila[4]} WHERE id = {fila[0]}")
            try:
                cursor.execute(sentenciaInsert)
            except mysql.connector.Error as error:
                if error.errno == 1062:  # errorcode.ER_DUP_ENTRY  # Duplicate entry error
                    cursor.execute(sentenciaUpdate)
                else:
                    print(error)

        # Eliminar filas que no están en la tabla.
        sentenciaSelect = (f"SELECT * FROM tipo_asignatura")
        cursor.execute(sentenciaSelect)
        for fila in cursor.fetchall():
            fila = [str(elemento) for elemento in fila]
            if fila not in datosTabla:
                cursor.execute(f"DELETE FROM tipo_asignatura WHERE id = {fila[0]}")


    @staticmethod
    def leer_datos_tabla(conexion):
        tipo_asignatura = []
        cursor = conexion.cursor()
        sql_lectura_datos: str = 'SELECT * FROM tipo_asignatura'
        cursor.execute(sql_lectura_datos)
        for registro in cursor.fetchall():
            tipo_asignatura.append(registro)
        cursor.close()
        # conexion.close()
        return tipo_asignatura


    @staticmethod
    def mostrar_datos(tipo_asignatura, ui, vistaTabla):
        vistaTabla.setRowCount(0)
        vistaTabla.setColumnCount(5)
        vistaTabla.setHorizontalHeaderLabels(["id", "nombre", "clave_tipo", "añadir", "factor"])

        for departamento in tipo_asignatura:
            fila = vistaTabla.rowCount()
            vistaTabla.insertRow(fila)
            vistaTabla.setItem(fila, 0, QTableWidgetItem(str(departamento[0]).replace('\n', '')))
            vistaTabla.setItem(fila, 1, QTableWidgetItem(str(departamento[1]).replace('\n', '')))
            vistaTabla.setItem(fila, 2, QTableWidgetItem(str(departamento[2]).replace('\n', '')))
            vistaTabla.setItem(fila, 3, QTableWidgetItem(str(departamento[3]).replace('\n', '')))
            vistaTabla.setItem(fila, 4, QTableWidgetItem(str(departamento[4]).replace('\n', '')))

        vistaTabla.resizeColumnsToContents()
        ui.nombreTabla.setText('Tipos de asignatura')
        return 'tipo_asignatura'
