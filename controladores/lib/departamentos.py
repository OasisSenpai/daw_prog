from PySide6.QtWidgets import QTableWidgetItem

import mysql.connector


class Departamentos:
    @staticmethod
    def actualizar_datos(cursor, datosTabla):
        # Actualizar o insertar filas.
        for fila in datosTabla:
            sentenciaInsert = (f"INSERT INTO departamentos (id, clave_dpto, nombre)\
                VALUES ({fila[0]}, '{fila[1]}', '{fila[2]}')")
            sentenciaUpdate = (f"UPDATE departamentos SET clave_dpto = '{fila[1]}', nombre = '{fila[2]}' WHERE id = {fila[0]}")
            try:
                cursor.execute(sentenciaInsert)
            except mysql.connector.Error as error:
                if error.errno == 1062:  # errorcode.ER_DUP_ENTRY  # Duplicate entry error
                    cursor.execute(sentenciaUpdate)
                else:
                    print(error)

        # Eliminar filas que no están en la tabla.
        sentenciaSelect = (f"SELECT * FROM departamentos")
        cursor.execute(sentenciaSelect)
        for fila in cursor.fetchall():
            fila = [str(elemento) for elemento in fila]
            if fila not in datosTabla:
                cursor.execute(f"DELETE FROM departamentos WHERE id = {fila[0]}")


    @staticmethod
    def leer_datos_tabla(conexion):
        departamentos = []
        cursor = conexion.cursor()
        sql_lectura_datos: str = 'SELECT * FROM departamentos'
        cursor.execute(sql_lectura_datos)
        for registro in cursor.fetchall():
            departamentos.append(registro)
        cursor.close()
        # conexion.close()
        return departamentos


    @staticmethod
    def mostrar_datos(departamentos, ui, vistaTabla):
        vistaTabla.setRowCount(0)
        vistaTabla.setColumnCount(3)
        vistaTabla.setHorizontalHeaderLabels(["id", "clave_dpto", "nombre"])

        for departamento in departamentos:
            fila = vistaTabla.rowCount()
            vistaTabla.insertRow(fila)
            vistaTabla.setItem(fila, 0, QTableWidgetItem(str(departamento[0])))
            vistaTabla.setItem(fila, 1, QTableWidgetItem(str(departamento[1])))
            vistaTabla.setItem(fila, 2, QTableWidgetItem(str(departamento[2])))

        vistaTabla.resizeColumnsToContents()
        ui.nombreTabla.setText('Departamentos')
        return 'departamentos'
