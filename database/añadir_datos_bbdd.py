from mysql import connector
from mysql.connector.connection import MySQLConnection

conexion: MySQLConnection = connector.connect(
    user = 'root',
    password = '',
    host = 'localhost',
    database = 'daw_prog'
)

cursor = conexion.cursor()


with open('database\\turnos.txt', 'r', encoding='utf-8') as fichero_turnos:
    cursor.execute('DELETE FROM turnos')
    for optativa in fichero_turnos.readlines():
        identificador, nombre = optativa.split(';')
        cursor.execute(f"INSERT INTO turnos (id, nombre) VALUES ({identificador}, '{nombre}')")

with open('database\\cursos.txt', 'r', encoding='utf-8') as fichero_cursos:
    cursor.execute('DELETE FROM cursos')
    for curso in fichero_cursos.readlines():
        identificador, nombre, grupo, turnos = curso.split(';')
        cursor.execute(f"INSERT INTO cursos (id, nombre, grupos, turnos)\
                         VALUES ({identificador}, '{nombre}', {grupo}, {turnos})")

with open('database\\optativas.txt', 'r', encoding='utf-8') as fichero_optativas:
    cursor.execute('DELETE FROM optativas')
    for optativa in fichero_optativas.readlines():
        identificador, nombre = optativa.split(';')
        cursor.execute(f"INSERT INTO optativas (id, nombre) VALUES ({identificador}, '{nombre}')")

with open('database\\departamentos.txt', 'r', encoding='utf-8') as fichero_departamentos:
    cursor.execute('DELETE FROM departamentos')
    for departamento in fichero_departamentos.readlines():
        identificador, clave, nombre = departamento.split(';')
        cursor.execute(f"INSERT INTO departamentos (id, clave_dpto, nombre)\
                         VALUES ({identificador}, '{clave}', '{nombre}')")

# modalidad = tipo_asignatura
with open('database\\modalidades.txt', 'r', encoding='utf-8') as fichero_modalidades:
    cursor.execute('DELETE FROM tipo_asignatura')
    for modalidad in fichero_modalidades.readlines():
        identificador, nombre, clave_tipo, aniadir, factor = modalidad.split(';')
        cursor.execute(f"INSERT INTO tipo_asignatura (id, nombre, clave_tipo, añadir, factor)\
                         VALUES ({identificador}, '{nombre}', '{clave_tipo}', {aniadir}, {factor})")

with open('database\\especialidades.txt', 'r', encoding='utf-8') as fichero_especialidades:
    cursor.execute('DELETE FROM especialidades')
    for especialidad in fichero_especialidades.readlines():
        identificador, nombre = especialidad.split(';')
        cursor.execute(f"INSERT INTO especialidades (id, nombre)\
                         VALUES ({identificador}, '{nombre}')")

with open('database\\materias.txt', 'r', encoding='utf-8') as fichero_materias:
    cursor.execute('DELETE FROM materias')
    cursor.execute('ALTER TABLE materias AUTO_INCREMENT = 1')
    for materia in fichero_materias.readlines():
        identificador, nombre, grupo, horas_semanales, id_curso,\
            id_tipo, id_depto, id_especialidad = materia.split(';')
        identificador = identificador if identificador != '' else 'NULL'
        nombre = nombre if nombre != '' else 'NULL'
        grupo = grupo if grupo != '' else 'NULL'
        horas_semanales = horas_semanales if horas_semanales != '' else 'NULL'
        id_curso = id_curso if id_curso != '' else 'NULL'
        id_tipo = id_tipo if id_tipo != '' else 'NULL'
        id_depto = id_depto if id_depto != '' else 'NULL'
        id_especialidad = id_especialidad if id_especialidad != '' else 'NULL'
        cursor.execute(f"INSERT INTO materias (id, nombre, id_curso, grupo, horas_semanales,\
                                               id_tipo, id_departamento, id_especialidad)\
                         VALUES ({identificador}, '{nombre}', {id_curso}, '{grupo}',\
                                 {horas_semanales}, {id_tipo}, {id_depto}, {id_especialidad})")


conexion.commit()
cursor.close()
conexion.close()
