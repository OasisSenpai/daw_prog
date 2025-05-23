from PySide6.QtWidgets import QTableWidgetItem

import mysql.connector


class Materias:
    @staticmethod
    def actualizar_datos(cursor, datosTabla):
        # Actualizar o insertar fila.
        for fila in datosTabla:
            sentenciaInsert = (f"INSERT INTO materias (id, nombre, id_curso, grupo,\
                                 horas_semanales, id_tipo, id_departamento, id_especialidad, id_optativa)\
                                 VALUES ({fila[0]}, '{fila[1]}', {fila[2]}, '{fila[3]}',\
                                 {fila[4] if fila[4] != '' else 'NULL'},\
                                 {fila[5] if fila[5] != '' else 'NULL'},\
                                 {fila[6] if fila[6] != '' else 'NULL'},\
                                 {fila[7] if fila[7] not in ('', 'None') else 'NULL'},\
                                 {fila[8] if fila[8] not in ('', 'None') else 'NULL'})")
            sentenciaUpdate = (f"UPDATE materias SET nombre = '{fila[1]}', grupo = '{fila[3]}',\
                                 horas_semanales = {fila[4] if fila[4] != '' else 'NULL'},\
                                 id_tipo = {fila[5] if fila[5] != '' else 'NULL'},\
                                 id_departamento = {fila[6] if fila[6] != '' else 'NULL'},\
                                 id_especialidad = {fila[7] if fila[7] not in ('', 'None') else 'NULL'},\
                                 id_optativa = {fila[8] if fila[8] not in ('', 'None') else 'NULL'}\
                                 WHERE id = {fila[0]} and id_curso = {fila[2]}")
            try:
                cursor.execute(sentenciaInsert)
            except mysql.connector.Error as error:
                if error.errno == 1062:  # errorcode.ER_DUP_ENTRY  # Duplicate entry error
                    cursor.execute(sentenciaUpdate)
                else:
                    print(error)

        # Eliminar filas que no están en la tabla.
        sentenciaSelect = (f"SELECT * FROM materias")
        cursor.execute(sentenciaSelect)
        for fila in cursor.fetchall():
            fila = [str(elemento) for elemento in fila]
            if fila not in datosTabla:
                cursor.execute(f"DELETE FROM materias WHERE id = {fila[0]}")
                print(f"DELETE FROM materias WHERE id = {fila[0]} and id_curso = {fila[2]}")


    @staticmethod
    def leer_datos_tabla(conexion):
        materias = []
        cursor = conexion.cursor()
        sql_lectura_datos: str = 'SELECT * FROM materias'
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
        vistaTabla.setHorizontalHeaderLabels(["id", "nombre", "id_curso", "grupo",\
            "horas_semanales", "id_tipo", "id_departamento", "id_especialidad", "id_optativa"])

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

        vistaTabla.resizeColumnsToContents()
        ui.nombreTabla.setText('Materias')
        return 'materias'
