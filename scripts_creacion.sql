-- Desactivar comprobación de claves foráneas:
SET FOREIGN_KEY_CHECKS=0;


-- Eliminación de tablas:
DROP TABLE IF EXISTS curso_contiene_materia;
DROP TABLE IF EXISTS materias;
DROP TABLE IF EXISTS especialidades;
DROP TABLE IF EXISTS tipo_asignatura;
DROP TABLE IF EXISTS optativas;
DROP TABLE IF EXISTS modalidades;
DROP TABLE IF EXISTS departamentos;
DROP TABLE IF EXISTS cursos;
DROP TABLE IF EXISTS turnos;


-- Creación tabla turnos:
CREATE TABLE turnos (
    id INT(1) NOT NULL PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL UNIQUE
);

-- Creación tabla cursos:
CREATE TABLE cursos (
    id INT(2) NOT NULL PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL UNIQUE,
    grupos INT(1) NOT NULL,
    turnos INT(1),
    CONSTRAINT fk_turnos
        FOREIGN KEY (turnos) REFERENCES turnos (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Creación tabla optativas:
CREATE TABLE optativas (
    id INT(2) NOT NULL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE
);

-- -- Creación tabla modalidades:
-- CREATE TABLE modalidades (
--     id INT(2) NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     nombre VARCHAR(30) NOT NULL
-- );

-- Creación tabla departamentos:
CREATE TABLE departamentos (
    id INT(2) NOT NULL PRIMARY KEY,
    clave_dpto VARCHAR(5) NOT NULL UNIQUE,
    nombre VARCHAR(30)
);

-- Creación tabla tipo_asignatura:
CREATE TABLE tipo_asignatura (
    id INT(2) NOT NULL PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL UNIQUE,
    clave_tipo VARCHAR(2) UNIQUE,
    añadir INT NOT NULL,
    factor DECIMAL(2,1) NOT NULL
);

-- Creación tabla especialidades:
CREATE TABLE especialidades (
    id INT(2) NOT NULL PRIMARY KEY,
    nombre VARCHAR(10) NOT NULL UNIQUE
);

-- Creación tabla materias:
CREATE TABLE materias (
    id INT(2) NOT NULL UNIQUE,
    nombre VARCHAR(30) NOT NULL,
    id_curso INT(2),
    grupo VARCHAR(20) NOT NULL,
    horas_semanales INT(2) DEFAULT 0,
    id_tipo INT(2),
    id_departamento INT(2),
    id_especialidad INT(2),
    -- id_modalidad INT(2),
    id_optativa INT(2),
    PRIMARY KEY (id, id_curso),
    CONSTRAINT fk_id_curso
        FOREIGN KEY (id_curso) REFERENCES cursos (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_id_tipo
        FOREIGN KEY (id_tipo) REFERENCES tipo_asignatura (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_id_departamento
        FOREIGN KEY (id_departamento) REFERENCES departamentos (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_id_especialidad
        FOREIGN KEY (id_especialidad) REFERENCES especialidades (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    -- CONSTRAINT fk_id_modalidad
    --     FOREIGN KEY (id_modalidad) REFERENCES modalidades (id)
    --     ON DELETE CASCADE
    --     ON UPDATE CASCADE,
    CONSTRAINT fk_id_optativa
        FOREIGN KEY (id_optativa) REFERENCES optativas (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- -- Creación tabla curso_contiene_materia:
-- CREATE TABLE curso_contiene_materia (
--     id_curso INT(2) NOT NULL,
--     id_materia INT(2) NOT NULL,
--     horas_semanales INT(2) NOT NULL,
--     PRIMARY KEY (id_curso, id_materia),
--     CONSTRAINT fk_id_curso
--         FOREIGN KEY (id_curso) REFERENCES cursos (id)
--         ON DELETE SET NULL
--         ON UPDATE RESTRICT,
--     CONSTRAINT fk_id_materia
--         FOREIGN KEY (id_materia) REFERENCES materias (id)
--         ON DELETE SET NULL
--         ON UPDATE RESTRICT
-- );