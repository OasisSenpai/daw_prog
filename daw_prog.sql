-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 21-05-2025 a las 09:33:40
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `daw_prog`
--

DELIMITER $$
--
-- Procedimientos
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `Pivot` (IN `tbl_name` VARCHAR(99), IN `base_cols` VARCHAR(99), IN `pivot_col` VARCHAR(64), IN `tally_col` VARCHAR(64), IN `where_clause` VARCHAR(99), IN `order_by` VARCHAR(99))  DETERMINISTIC SQL SECURITY INVOKER BEGIN
    -- Establecer explícitamente la colación para todas las cadenas
    SET NAMES utf8mb4 COLLATE utf8mb4_spanish2_ci;
    
    -- Find the distinct values
    -- Build the SUM()s
    SET @subq = CONCAT('SELECT DISTINCT ', pivot_col, ' AS val ',
                    ' FROM ', tbl_name, ' ', where_clause, ' ORDER BY 1') COLLATE utf8mb4_spanish2_ci;
    
    SET @cc1 = CONVERT("CONCAT('SUM(IF(&p = ', &v, ', &t, 0)) AS ', &v)" USING utf8mb4) COLLATE utf8mb4_spanish2_ci;
    SET @cc2 = REPLACE(@cc1, '&p', pivot_col) COLLATE utf8mb4_spanish2_ci;
    SET @cc3 = REPLACE(@cc2, '&t', tally_col) COLLATE utf8mb4_spanish2_ci;
    
    SET @qval = CONCAT("'\"', val, '\"'") COLLATE utf8mb4_spanish2_ci;
    SET @cc4 = REPLACE(@cc3, '&v', @qval) COLLATE utf8mb4_spanish2_ci;
    
    SET SESSION group_concat_max_len = 10000;   -- just in case
    SET @stmt = CONCAT(
            'SELECT  GROUP_CONCAT(', @cc4, ' SEPARATOR ",\n")  INTO @sums',
            ' FROM ( ', @subq, ' ) AS top') COLLATE utf8mb4_spanish2_ci;
    
    PREPARE _sql FROM @stmt;
    EXECUTE _sql;                      -- Intermediate step: build SQL for columns
    DEALLOCATE PREPARE _sql;
    
    -- Construct the query and perform it
    SET @stmt2 = CONCAT(
            'SELECT ',
                base_cols, ',\n',
                @sums,
                ',\n SUM(', tally_col, ') AS Total'
            '\n FROM ', tbl_name, ' ',
            where_clause,
            ' GROUP BY ', base_cols,
            '\n WITH ROLLUP',
            '\n', order_by
        ) COLLATE utf8mb4_spanish2_ci;
        
        
    PREPARE _sql FROM @stmt2;
    -- EXECUTE _sql;                     -- The resulting pivot table ouput
    SELECT @stmt2;
    DEALLOCATE PREPARE _sql;
    -- For debugging / tweaking, SELECT the various @variables after CALLing.
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cursos`
--

CREATE TABLE `cursos` (
  `id` int(2) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `grupos` int(1) NOT NULL,
  `turnos` int(1) DEFAULT NULL COMMENT 'FK: turnos'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

--
-- Volcado de datos para la tabla `cursos`
--

INSERT INTO `cursos` (`id`, `nombre`, `grupos`, `turnos`) VALUES
(1, '1º ESO', 4, 1),
(2, '2ª ESO', 4, 1),
(3, '3º ESO', 3, 1),
(4, '4º ESO', 3, 1),
(5, '1º Bachilerato', 5, 1),
(6, '2º Bachillerato', 4, 1),
(7, '1º GM SMR', 3, 1),
(8, '2º GM SMR', 3, 1),
(9, '1º GS ASIR', 2, 1),
(10, '2º GS ASIR', 2, 1),
(11, '1º GS DAM', 2, 1),
(12, '2º GS DAM', 2, 1),
(13, '1º GM ACOM', 1, 1),
(14, '2º GM ACOM', 1, 1),
(15, '1º GSCINT', 2, 1),
(16, '2º GSCINT', 2, 1),
(17, '1º GSTYL', 2, 1),
(18, '2º GSTYL', 2, 1),
(19, '1º GB Admon', 1, 1),
(20, '2º GB Admon', 1, 1),
(21, '1º GM ADTVA', 2, 1),
(22, '2º GM ADTVA', 2, 1),
(23, '1º GS AFI', 3, 1),
(24, '2º GS AFI', 3, 1),
(25, '1º GS ASD', 1, 1),
(26, '2º GS ASD', 1, 1),
(27, '1º GB Forestal', 1, 1),
(28, '2º GB Forestal', 1, 1),
(30, 'Varios', 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamentos`
--

CREATE TABLE `departamentos` (
  `id` int(2) NOT NULL,
  `clave_dpto` varchar(5) NOT NULL,
  `nombre` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

--
-- Volcado de datos para la tabla `departamentos`
--

INSERT INTO `departamentos` (`id`, `clave_dpto`, `nombre`) VALUES
(1, 'ByG', 'Biología y Geología\n'),
(2, 'EDF', 'Educación Física\n'),
(3, 'Fra', 'Francés\n'),
(4, 'GyH', 'Geografía e Historia\n'),
(5, 'LcyL', 'Lengua Castellana y Literatura'),
(6, 'Ing', 'Inglés\n'),
(7, 'Mat', 'Matemáticas\n'),
(8, 'Mus', 'Música\n'),
(9, 'Pla', 'Plástica\n'),
(10, 'Rel', 'Religión\n'),
(11, 'Tec', 'Tecnología\n'),
(12, 'Clas', 'Clásica\n'),
(13, 'Fil', 'Filosofía\n'),
(14, 'FyQ', 'Física y Química\n'),
(15, 'Eco', 'Economía\n'),
(16, 'Inf', 'Informática y Comunicaciones\n'),
(17, 'Com', 'Comercio\n'),
(18, 'Adm', 'Administración\n'),
(19, 'FOL', 'FOL\n'),
(20, 'For', 'Forestal\n'),
(30, 'PDT', 'Pendiente\n');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `especialidades`
--

CREATE TABLE `especialidades` (
  `id` int(2) NOT NULL,
  `nombre` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

--
-- Volcado de datos para la tabla `especialidades`
--

INSERT INTO `especialidades` (`id`, `nombre`) VALUES
(1, 'B1\n'),
(2, 'B2\n'),
(3, 'B5\n'),
(4, 'INF\n'),
(30, 'NULL'),
(5, 'SA\n'),
(6, 'SA/TA\n'),
(7, 'SAI\n'),
(8, 'SAI/INF\n'),
(9, 'SC\n'),
(10, 'SC/TC\n'),
(11, 'TA\n'),
(12, 'TC\n');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `materias`
--

CREATE TABLE `materias` (
  `id` int(2) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `id_curso` int(2) NOT NULL COMMENT 'FK: cursos',
  `grupo` varchar(20) NOT NULL,
  `horas_semanales` int(2) DEFAULT 0,
  `id_tipo` int(2) DEFAULT NULL COMMENT 'FK: tipo_asignatura',
  `id_departamento` int(2) DEFAULT NULL COMMENT 'FK: departamentos',
  `id_especialidad` int(2) DEFAULT NULL COMMENT 'FK: especialidades',
  `id_optativa` int(2) DEFAULT NULL COMMENT 'FK: optativas'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

--
-- Volcado de datos para la tabla `materias`
--

INSERT INTO `materias` (`id`, `nombre`, `id_curso`, `grupo`, `horas_semanales`, `id_tipo`, `id_departamento`, `id_especialidad`, `id_optativa`) VALUES
(1, 'Biología y Geología', 1, 'Comunes', 3, 2, 1, 30, NULL),
(2, 'Educación Física', 1, 'Comunes', 2, 1, 2, 30, NULL),
(3, 'Francés 2ª lengua extranjera: ', 1, 'Optativas', 2, 3, 3, 30, NULL),
(4, 'Geografía e Historia', 1, 'Comunes', 4, 2, 4, 30, NULL),
(5, 'Lengua Castellana y Literatura', 1, 'Comunes', 5, 1, 5, 30, NULL),
(6, 'Lengua extranjera: Inglés', 1, 'Idiomas', 4, 2, 6, 30, NULL),
(7, 'Matemáticas', 1, 'Comunes', 4, 1, 7, 30, NULL),
(8, 'Música', 1, 'Comunes', 2, 2, 8, 30, NULL),
(9, 'Proyectos de Artes Plásticas y', 1, 'Optativas', 2, 3, 9, 30, NULL),
(10, 'Religión Católica', 1, 'Religión', 1, 1, 10, 30, NULL),
(11, 'Tecnología y Digitalización', 1, 'Comunes', 2, 1, 11, 30, NULL),
(12, 'Cultura Clásica', 2, 'Optativas', 2, 3, 12, 30, NULL),
(13, 'Desarrollo Digital', 2, 'Optativas', 2, 3, 11, 30, NULL),
(14, 'Educación en Valores Cívicos y', 2, 'Comunes', 2, 1, 13, 30, NULL),
(15, 'Educación Física', 2, 'Comunes', 2, 1, 2, 30, NULL),
(16, 'Educación Plástica Visual y A', 2, 'Comunes', 2, 1, 9, 30, NULL),
(17, 'Física y Química PL', 2, 'Comunes', 3, 6, 1, 30, NULL),
(18, 'Física y Química', 2, 'Comunes', 3, 1, 14, 30, NULL),
(19, 'Francés 2ª lengua extranjera:', 2, 'Optativas', 2, 3, 3, 30, NULL),
(20, 'Geografía e Historia', 2, 'Comunes', 3, 2, 4, 30, NULL),
(21, 'Lengua Castellana y Literatura', 2, 'Comunes', 4, 1, 5, 30, NULL),
(22, 'Lengua extranjera: Inglés', 2, 'Idiomas', 4, 2, 6, 30, NULL),
(23, 'Matemáticas', 2, 'Comunes', 4, 1, 7, 30, NULL),
(24, 'Música', 2, 'Comunes', 2, 2, 8, 30, NULL),
(25, 'Religión Católica', 2, 'Religión', 1, 1, 10, 30, NULL),
(26, 'Ámbito Científico-Tecnológico', 3, 'Ámbitos DIVER / PMAR', 9, 5, NULL, 30, NULL),
(27, 'Ámbito Lingüístico y Social', 3, 'Ámbitos DIVER / PMAR', 8, 5, NULL, 30, NULL),
(28, 'Biología y Geología', 3, 'Comunes', 3, 2, 1, 30, NULL),
(29, 'Educación Física', 3, 'Comunes', 2, 2, 2, 30, NULL),
(30, 'Educación Plástica Visual y A', 3, 'Comunes', 2, 1, 9, 30, NULL),
(31, 'Emprendimiento Sostenibilidad', 3, 'Optativas', 2, 3, 15, 30, NULL),
(32, 'Física y Química', 3, 'Comunes', 3, 1, 14, 30, NULL),
(33, 'Francés 2ª lengua extranjera:', 3, 'Optativas', 2, 4, 3, 30, NULL),
(34, 'Geografía e Historia', 3, 'Comunes', 3, 2, 4, 30, NULL),
(35, 'Lengua Castellana y Literatura', 3, 'Comunes', 4, 1, 5, 30, NULL),
(36, 'Lengua extranjera: Inglés', 3, 'Idiomas', 3, 12, 6, 30, NULL),
(37, 'Matemáticas', 3, 'Comunes', 4, 1, 7, 30, NULL),
(38, 'Música Activa Movimiento y Fo', 3, 'Optativas', 2, 3, 8, 30, NULL),
(39, 'Religión Católica', 3, 'Religión', 1, 1, 10, 30, NULL),
(40, 'Tecnología y Digitalización', 3, 'Comunes', 2, 1, 11, 30, NULL),
(41, 'Ámbito Científico-Tecnológico', 4, 'Ámbitos DIVER / PMAR', 9, 5, NULL, 30, NULL),
(42, 'Ámbito Lingüístico y Social', 4, 'Ámbitos DIVER / PMAR', 8, 5, NULL, 30, NULL),
(43, 'Artes Escénicas Danza y Folcl', 4, 'Optativas', 2, 3, 5, 30, NULL),
(44, 'Biología y Geología', 4, 'Opción 2', 3, 3, 1, 30, NULL),
(45, 'Cultura Científica', 4, 'Optativas', 2, 3, 1, 30, NULL),
(46, 'Digitalización', 4, 'Opción 1', 3, 3, 11, 30, NULL),
(47, 'Economía y Emprendimiento', 4, 'Opción 3', 3, 3, 15, 30, NULL),
(48, 'Educación Física', 4, 'Comunes', 2, 2, 2, 30, NULL),
(49, 'Expresión Artística', 4, 'Opción 2', 3, 3, 9, 30, NULL),
(50, 'Filosofía', 4, 'Optativas', 2, 3, 13, 30, NULL),
(51, 'Física y Química', 4, 'Opción 3', 3, 3, 14, 30, NULL),
(52, 'Francés 2ª lengua extranjera: ', 4, 'Opción 1', 3, 4, 3, 30, NULL),
(53, 'Geografía e Historia', 4, 'Comunes', 3, 2, 4, 30, NULL),
(54, 'Latín', 4, 'Opción 2', 3, 3, 12, 30, NULL),
(55, 'Lengua Castellana y Literatura', 4, 'Comunes', 4, 1, 5, 30, NULL),
(56, 'Lengua extranjera: Inglés', 4, 'Idiomas', 4, 2, 6, 30, NULL),
(57, 'Matemáticas A/B', 4, 'Matemáticas', 4, 1, 7, 30, NULL),
(58, 'Música', 4, 'Opción 3', 3, 3, 8, 30, NULL),
(59, 'Proyectos de Robótica', 4, 'Optativas', 2, 4, 11, 30, NULL),
(60, 'Religión Católica', 4, 'Religión', 1, 1, 10, 30, NULL),
(61, 'Anatomía Aplicada', 5, 'Optativas', 4, 7, 1, 30, NULL),
(62, 'Biología', 5, 'Específica de opción', 4, 7, 1, 30, NULL),
(63, 'Educación Física', 5, 'Comunes', 2, 1, 2, 30, NULL),
(64, 'Mat. aplic. Ciencias Soc. I', 5, 'Específicas obligato', 4, 7, 7, 1, NULL),
(65, 'Historia del Mundo Contemporán', 5, 'Específica de opción', 4, 8, 4, 30, NULL),
(66, 'Matemáticas I', 5, 'Específicas obligato', 4, 8, 7, 1, NULL),
(67, 'Lengua Castellana y Literatura', 5, 'Comunes', 4, 1, 5, 30, NULL),
(68, 'Artes escénicas I', 5, 'Específica de opción', 4, 7, 5, 30, NULL),
(69, 'Literatura universal', 5, 'Específica de opción', 4, 7, 5, 30, NULL),
(70, 'Inglés Lengua extranjera I: ', 5, 'Idiomas', 3, 1, 6, 30, NULL),
(71, 'Francés 2ª lengua extranjera I', 5, 'Optativas', 4, 8, 3, 2, NULL),
(72, 'Unión Europea', 5, 'Optativas', 4, 11, 4, 3, NULL),
(73, 'Análisis musical I', 5, 'Específicas obligato', 4, 7, 8, 30, NULL),
(74, 'Lenguaje y Práctica Musical', 5, 'Específica de opción', 4, 7, 8, 30, NULL),
(75, 'Proyectos Artísticos', 5, 'Específica de opción', 4, 7, 8, 30, NULL),
(76, 'Coro y Técnica Vocal I', 5, 'Optativas', 4, 7, 8, 30, NULL),
(77, 'Dibujo Artístico I', 5, 'Específicas obligato', 4, 7, 9, 30, NULL),
(78, 'Dibujo Técnico Aplicado a Arte', 5, 'Específica de opción', 4, 7, 9, 30, NULL),
(79, 'Dibujo Técnico II', 5, 'Específica de opción', 4, 7, 9, 30, NULL),
(80, 'Volumen', 5, 'Específica de opción', 4, 7, 9, 30, NULL),
(81, 'Cultura audiovisual', 5, 'Optativas', 4, 8, 9, 30, NULL),
(82, 'Religión Católica', 5, 'Religión', 2, 1, 10, 30, NULL),
(83, 'Tecnología e Ingeniería I', 5, 'Optativas', 4, 7, 11, 30, NULL),
(84, 'Desarrollo Digital', 5, 'Optativas', 4, 8, 30, 30, NULL),
(85, 'Latín I', 5, 'Específicas obligato', 4, 7, 12, 30, NULL),
(86, 'Filosofía', 5, 'Comunes', 3, 1, 13, 30, NULL),
(87, 'Psicología', 5, 'Optativas', 4, 8, 30, 30, NULL),
(88, 'Física y Química', 5, 'Específica de opción', 4, 8, 14, 30, NULL),
(89, 'Economía', 5, 'Específica de opción', 4, 7, 15, 30, NULL),
(90, 'Biología', 6, 'Específica de opción', 4, 7, 1, 30, NULL),
(91, 'Geología y ciencias ambientale', 6, 'Específica de opción', 4, 7, 1, 30, NULL),
(92, 'Historia de España', 6, 'Comunes', 3, 1, 4, 30, NULL),
(93, 'Historia del arte', 6, 'Específica de opción', 4, 7, 4, 30, NULL),
(94, 'Geografía', 6, 'Específica de opción', 4, 8, 4, 30, NULL),
(95, 'Historia de la música y la dan', 6, 'Optativas', 4, 7, 4, 30, NULL),
(96, 'Lengua Castellana y Literatura', 6, 'Comunes', 4, 1, 5, 30, NULL),
(97, 'Artes escénicas II', 6, 'Específicas obligato', 4, 7, 5, 30, NULL),
(98, 'Literatura dramática', 6, 'Optativas', 4, 7, 5, 30, NULL),
(99, 'Inglés Lengua extranjera II: ', 6, 'Idiomas', 4, 1, 6, 30, NULL),
(100, 'Matemáticas II', 6, 'Específicas obligato', 4, 7, 7, 30, NULL),
(101, 'Mat. aplic. Ciencias Soc. II', 6, 'Específicas obligato', 4, 7, 7, 30, NULL),
(102, 'Análisis musical II', 6, 'Específicas obligato', 4, 7, 8, 30, NULL),
(103, 'Coro y técnica vocal II', 6, 'Optativas', 4, 7, 8, 30, NULL),
(104, 'Dibujo Artístico II', 6, 'Específicas obligato', 4, 7, 9, 30, NULL),
(105, 'Dibujo técnico aplicado a arte', 6, 'Específica de opción', 4, 7, 9, 30, NULL),
(106, 'Dibujo Técnico II', 6, 'Específica de opción', 4, 7, 9, 30, NULL),
(107, 'Tecnología e Ingeniería II', 6, 'Específica de opción', 4, 7, 11, 30, NULL),
(108, 'Latín II', 6, 'Específicas obligato', 4, 7, 12, 30, NULL),
(109, 'Historia de la filosofía', 6, 'Comunes', 3, 1, 13, 30, NULL),
(110, 'Física', 6, 'Específica de opción', 4, 7, 14, 30, NULL),
(111, 'Química', 6, 'Específica de opción', 4, 7, 14, 30, NULL),
(112, 'Empresa y diseño de modelos de', 6, 'Específica de opción', 4, 7, 15, 30, NULL),
(113, 'Diseño', 6, 'Optativas', 4, 7, 30, 30, NULL),
(114, 'Fundamentos artísticos', 6, 'Específica de opción', 4, 7, 30, 30, NULL),
(115, 'Técnicas de expresión gráfico-', 6, 'Optativas', 4, 7, 30, 30, NULL),
(116, 'Creación de contenidos artísti', 6, 'Optativas', 4, 8, 30, 30, NULL),
(117, 'Fundamentos de administración', 6, 'Optativas', 4, 8, 30, 30, NULL),
(118, 'Redes Locales', 7, 'NULL', 5, 1, 16, 4, NULL),
(119, 'Aplicaciones web', 7, 'NULL', 5, 1, 16, 4, NULL),
(120, 'Seguridad Informática', 8, 'NULL', 5, 1, 16, 4, NULL),
(121, 'Servicios en red', 8, 'NULL', 6, 1, 16, 4, NULL),
(122, 'Planificación y Admón Redes', 9, 'NULL', 5, 1, 16, 4, NULL),
(123, 'Gestión de Bases de Datos', 9, 'NULL', 4, 1, 16, 4, NULL),
(124, 'Lenguaje de marcas', 9, 'NULL', 3, 1, 16, 4, NULL),
(125, 'Servicios de red e internet', 10, 'NULL', 7, 1, 16, 4, NULL),
(126, 'Implantación de aplicaciones w', 10, 'NULL', 5, 1, 16, 4, NULL),
(127, 'Admón. Sistemas gestores BBDD', 10, 'NULL', 3, 1, 16, 4, NULL),
(128, 'Seguridad y alta disponibilida', 10, 'NULL', 5, 1, 16, 4, NULL),
(129, 'Bases de datos', 11, 'NULL', 5, 1, 16, 4, NULL),
(130, 'Programación', 11, 'NULL', 6, 1, 16, 4, NULL),
(131, 'Lenguaje de marcas', 11, 'NULL', 3, 1, 16, 4, NULL),
(132, 'Entornos de desarrollo', 11, 'NULL', 2, 1, 16, 4, NULL),
(133, 'Acceso a datos', 12, 'NULL', 7, 1, 16, 4, NULL),
(134, 'Programación Multimedia y disp', 12, 'NULL', 5, 1, 16, 4, NULL),
(135, 'Programación servicios proceso', 12, 'NULL', 3, 1, 16, 4, NULL),
(136, 'Técnica contable', 21, 'NULL', 5, 1, 18, 5, NULL),
(137, 'Operaciones Aux. Tesorería', 21, 'NULL', 5, 1, 18, 5, NULL),
(138, 'Tratamiento Docum. Contable', 22, 'NULL', 6, 1, 18, 5, NULL),
(139, 'Gest Docum Jurídica Empre', 23, 'NULL', 2, 1, 18, 5, NULL),
(140, 'RRHH Responsabilidad Civil Cor', 23, 'NULL', 2, 1, 18, 5, NULL),
(141, 'Proceso integral Actividad Com', 23, 'NULL', 6, 1, 18, 5, NULL),
(142, 'Gestión RRHH', 24, 'NULL', 3, 1, 18, 5, NULL),
(143, 'Gestión Financiera', 24, 'NULL', 7, 1, 18, 5, NULL),
(144, 'Contabilidad y Fiscalidad', 24, 'NULL', 5, 1, 18, 5, NULL),
(145, 'Simulación Empresarial', 24, 'NULL', 5, 2, 18, 5, NULL),
(146, 'Gest. Docum. Jurídica Empre.', 25, 'NULL', 2, 1, 18, 5, NULL),
(147, 'RRHH Responsabilidad Civil Cor', 25, 'NULL', 4, 1, 18, 5, NULL),
(148, 'Proyecto intermodular de desar', 11, 'NULL', 1, 1, 16, 30, NULL),
(149, 'Proceso integral Actividad Com', 25, 'NULL', 6, 1, 18, 5, NULL),
(150, 'Organización de eventos empres', 26, 'NULL', 8, 1, 18, 5, NULL),
(151, 'Protocolo empresarial', 26, 'NULL', 7, 2, 18, 5, NULL),
(152, 'IPE II', 30, 'NULL', 2, 1, 18, 5, NULL),
(153, 'Digitalización aplicada al sec', 21, 'NULL', 2, 1, 18, 6, NULL),
(154, 'Sostenibilidad aplicada al sis', 21, 'NULL', 1, 1, 18, 6, NULL),
(155, 'Proyecto intermodular', 21, 'NULL', 1, 1, 18, 6, NULL),
(156, 'Proyecto intermodular', 22, 'NULL', 1, 1, 18, 6, NULL),
(157, 'Empresa en el Aula', 22, 'NULL', 7, 1, 18, 6, NULL),
(158, 'FE', 21, 'NULL', 1, 1, 18, 6, NULL),
(159, 'FE', 22, 'NULL', 1, 1, 18, 6, NULL),
(160, 'Digitalización aplicada al sec', 23, 'NULL', 2, 1, 18, 6, NULL),
(161, 'Sostenibilidad aplicada al sis', 23, 'NULL', 1, 1, 18, 6, NULL),
(162, 'Proyecto intermodular', 23, 'NULL', 1, 1, 18, 6, NULL),
(163, 'Proyecto intermodular', 24, 'NULL', 1, 1, 18, 6, NULL),
(164, 'FE', 23, 'NULL', 1, 1, 18, 6, NULL),
(165, 'FE', 24, 'NULL', 1, 1, 18, 6, NULL),
(166, 'Digitalización aplicada al sec', 25, 'NULL', 2, 1, 18, 6, NULL),
(167, 'Sostenibilidad aplicada al sis', 25, 'NULL', 1, 1, 18, 6, NULL),
(168, 'Proyecto intermodular', 25, 'NULL', 1, 1, 18, 6, NULL),
(169, 'FE', 25, 'NULL', 1, 1, 18, 6, NULL),
(170, 'FE', 26, 'NULL', 1, 1, 18, 6, NULL),
(171, 'BILINGÜE ', 30, 'NULL', 2, 1, 18, 6, NULL),
(172, 'AULA EMPRENDEDORA', 30, 'NULL', 2, 1, 18, 6, NULL),
(173, 'COORDINADOR', 30, 'NULL', 2, 1, 18, 6, NULL),
(174, 'Montaje Mantenimiento Equipos', 7, 'NULL', 6, 1, 16, 7, NULL),
(175, 'Aplicaciones Ofimáticas', 8, 'NULL', 6, 1, 16, 7, NULL),
(176, 'Sistemas Operativos en red', 8, 'NULL', 5, 1, 16, 7, NULL),
(177, 'Implantación Sistemas Operativ', 9, 'NULL', 6, 1, 16, 7, NULL),
(178, 'Fundamentos del Hardware', 9, 'NULL', 3, 1, 16, 7, NULL),
(179, 'Admón sistemas Operativos', 10, 'NULL', 7, 1, 16, 7, NULL),
(180, 'Sistemas informáticos', 11, 'NULL', 5, 1, 16, 7, NULL),
(181, 'Desarrollo de interfaces', 12, 'NULL', 7, 1, 16, 7, NULL),
(182, 'Sistemas gestión empresarial', 12, 'NULL', 5, 1, 16, 7, NULL),
(183, 'Proyecto intermodular de admin', 7, 'NULL', 1, 1, 16, 8, NULL),
(184, 'Digitalización aplicada a los ', 7, 'NULL', 2, 1, 16, 8, NULL),
(185, 'Sostenibilidad aplicada al sis', 7, 'NULL', 1, 1, 16, 8, NULL),
(186, 'Sistemas Operativos Monopuesto', 7, 'NULL', 5, 1, 16, 8, NULL),
(187, 'Proyecto intermodular de admin', 8, 'NULL', 1, 1, 16, 8, NULL),
(188, 'FE', 7, 'NULL', 1, 1, 16, 8, NULL),
(189, 'FE', 8, 'NULL', 1, 1, 16, 8, NULL),
(190, 'Proyecto intermodular de admin', 9, 'NULL', 1, 1, 16, 8, NULL),
(191, 'Digitalización aplicada a los ', 9, 'NULL', 2, 1, 16, 8, NULL),
(192, 'Sostenibilidad aplicada al sis', 9, 'NULL', 1, 1, 16, 8, NULL),
(193, 'Proyecto intermodular de admin', 10, 'NULL', 1, 1, 16, 8, NULL),
(194, 'FE', 9, 'NULL', 1, 1, 16, 8, NULL),
(195, 'FE', 10, 'NULL', 1, 1, 16, 8, NULL),
(196, 'Sostenibilidad aplicada al sis', 11, 'NULL', 1, 1, 16, 8, NULL),
(197, 'Digitalización aplicada a los ', 11, 'NULL', 2, 1, 16, 8, NULL),
(198, 'Proyecto intermodular de admin', 12, 'NULL', 1, 1, 16, 8, NULL),
(199, 'FE', 11, 'NULL', 1, 1, 16, 8, NULL),
(200, 'FE', 12, 'NULL', 1, 1, 16, 8, NULL),
(201, 'Mantenimiento Equipos', 30, 'NULL', 2, 1, 16, 8, NULL),
(202, 'Web centro', 30, 'NULL', 2, 1, 16, 8, NULL),
(203, 'Directiva', 30, 'NULL', 33, 1, 16, 8, NULL),
(204, 'Coordinación', 30, 'NULL', 2, 1, 16, 8, NULL),
(205, 'Márketing en la Act. Comercial', 13, 'NULL', 5, 1, 17, 9, NULL),
(206, 'Procesos de ventas', 13, 'NULL', 4, 1, 17, 9, NULL),
(207, 'Gestión de pequeño comercio', 14, 'NULL', 8, 1, 17, 9, NULL),
(208, 'Venta técnica', 14, 'NULL', 5, 1, 17, 9, NULL),
(209, 'GEFE', 15, 'NULL', 6, 2, 17, 9, NULL),
(210, 'GACI', 15, 'NULL', 6, 2, 17, 9, NULL),
(211, 'Márketing internacional', 16, 'NULL', 7, 1, 17, 9, NULL),
(212, 'Negociación internacional', 16, 'NULL', 5, 1, 17, 9, NULL),
(213, 'Financiación internacional', 16, 'NULL', 6, 1, 17, 9, NULL),
(214, 'Medios pagos internacionales', 16, 'NULL', 5, 1, 17, 9, NULL),
(215, 'Logísitica Almacenamiento', 17, 'NULL', 6, 1, 17, 9, NULL),
(216, 'Gestión Adtva  Transporte y Lo', 18, 'NULL', NULL, 1, 17, 9, NULL),
(217, 'Comercialización T y L', 18, 'NULL', 9, 2, 17, 9, NULL),
(218, 'Organización Transporte viajer', 18, 'NULL', 5, 2, 17, 9, NULL),
(219, 'Organización Transporte Merca', 18, 'NULL', 5, 2, 17, 9, NULL),
(220, 'Digitalización', 13, 'NULL', 2, 1, 17, 10, NULL),
(221, 'Sostenibilidad', 13, 'NULL', 1, 1, 17, 10, NULL),
(222, 'Proyecto', 13, 'NULL', 1, 1, 17, 10, NULL),
(223, 'Proyecto', 14, 'NULL', 1, 1, 17, 10, NULL),
(224, 'FE', 13, 'NULL', 1, 1, 17, 10, NULL),
(225, 'FE', 14, 'NULL', 1, 1, 17, 10, NULL),
(226, 'Digitalización', 15, 'NULL', 2, 1, 17, 10, NULL),
(227, 'Sostenibilidad', 15, 'NULL', 1, 1, 17, 10, NULL),
(228, 'Proyecto', 15, 'NULL', 1, 1, 17, 10, NULL),
(229, 'Proyecto', 16, 'NULL', 1, 1, 17, 10, NULL),
(230, 'FE', 15, 'NULL', 1, 1, 17, 10, NULL),
(231, 'FE', 16, 'NULL', 1, 1, 17, 10, NULL),
(232, 'Digitalización', 17, 'NULL', 6, 1, 17, 10, NULL),
(233, 'Sostenibilidad', 17, 'NULL', 1, 1, 17, 10, NULL),
(234, 'Proyecto', 17, 'NULL', 1, 1, 17, 10, NULL),
(235, 'Proyecto', 18, 'NULL', 1, 1, 17, 10, NULL),
(236, 'FE', 17, 'NULL', 1, 1, 17, 10, NULL),
(237, 'BILINGÜE', 30, 'NULL', 4, 1, 17, 10, NULL),
(238, 'Coordinación', 30, 'NULL', 2, 1, 17, 10, NULL),
(239, 'Tratamiento informático de dat', 19, 'NULL', 8, 1, 18, 11, NULL),
(240, 'Técnicas administrativas básic', 19, 'NULL', 6, 1, 18, 11, NULL),
(241, 'Archivo y comunicación', 19, 'NULL', 4, 1, 18, 11, NULL),
(242, 'Proyecto Intermodular', 19, 'NULL', 1, 1, 18, 11, NULL),
(243, 'Tutoría', 20, 'NULL', 1, 1, 18, 11, NULL),
(244, 'Aplicaciones básicas ofimática', 20, 'NULL', 8, 1, 18, 11, NULL),
(245, 'Atención al cliente', 20, 'NULL', 3, 1, 18, 11, NULL),
(246, 'Preparación pedidos y ventas', 20, 'NULL', 4, 1, 18, 11, NULL),
(247, 'Tutoría', 20, 'NULL', 1, 1, 18, 11, NULL),
(248, 'Proyecto Intermodular', 20, 'NULL', 1, 1, 18, 11, NULL),
(249, 'FE', 20, 'NULL', 1, 1, 18, 11, NULL),
(250, 'Operaciones Adtvas. CV', 21, 'NULL', 4, 1, 18, 11, NULL),
(251, 'Tratamiento informático Inform', 21, 'NULL', 7, 1, 18, 11, NULL),
(252, 'CEAC', 22, 'NULL', 6, 1, 18, 11, NULL),
(253, 'Empresa y Administración', 22, 'NULL', 5, 1, 18, 11, NULL),
(254, 'Operaciones Adtvas. RRHH', 22, 'NULL', 6, 1, 18, 11, NULL),
(255, 'Ofimática y Proceso Informació', 23, 'NULL', 7, 1, 18, 11, NULL),
(256, 'Comunicación y atención Clien', 23, 'NULL', 4, 1, 18, 11, NULL),
(257, 'Ofimática y Proceso Informació', 25, 'NULL', 7, 1, 18, 11, NULL),
(258, 'Comunicación y atención Clien', 25, 'NULL', 4, 1, 18, 11, NULL),
(259, 'Gestión Avanzada a la Informac', 26, 'NULL', 7, 1, 18, 11, NULL),
(260, 'Gestión de Compras', 13, 'NULL', 3, 1, 17, 12, NULL),
(261, 'Aplicaciones Informáticas Com.', 13, 'NULL', 4, 1, 17, 12, NULL),
(262, 'Dinamización punto de venta', 13, 'NULL', 5, 1, 17, 12, NULL),
(263, 'Técnicas de almacén', 14, 'NULL', 6, 1, 17, 12, NULL),
(264, 'Servicios de atención comercia', 14, 'NULL', 5, 1, 17, 12, NULL),
(265, 'Comercio electrónico', 14, 'NULL', 6, 1, 17, 12, NULL),
(266, 'Transporte internacional Merc.', 15, 'NULL', 5, 2, 17, 12, NULL),
(267, 'Logísitica Almacenamiento', 15, 'NULL', 4, 1, 17, 12, NULL),
(268, 'Sistemas Información mercados', 16, 'NULL', 4, 1, 17, 12, NULL),
(269, 'comercio digital internacional', 16, 'NULL', 3, 1, 17, 12, NULL),
(270, 'Transporte internacional Merc', 17, 'NULL', 5, 1, 17, 12, NULL),
(271, 'GACI', 17, 'NULL', 4, 1, 17, 12, NULL),
(272, 'Logistica de Aprovisionamiento', 18, 'NULL', 6, 2, 17, 12, NULL),
(273, 'FE', 18, 'NULL', 1, 1, 17, 12, NULL),
(274, 'Iniciación Actividad Emprended', 30, 'NULL', 2, 1, 17, 12, NULL),
(275, 'Digitalización Administración', 30, 'NULL', 2, 1, 17, 12, NULL),
(276, 'Gestión Logística Comercial', 24, 'NULL', 5, 1, 18, 12, NULL),
(277, 'IPE II', 28, 'NULL', 2, 1, 19, 30, NULL),
(278, 'IPE I', 27, 'NULL', 2, 1, 19, 30, NULL),
(279, 'IPE I', 19, 'NULL', 2, 1, 19, 30, NULL),
(280, 'IPE II', 20, 'NULL', 2, 1, 19, 30, NULL),
(281, 'IPE I', 21, 'NULL', 3, 1, 19, 30, NULL),
(282, 'IPE I', 23, 'NULL', 3, 1, 19, 30, NULL),
(283, 'IPE I', 25, 'NULL', 3, 1, 19, 30, NULL),
(284, 'IPE I', 13, 'NULL', 3, 1, 19, 30, NULL),
(285, 'IPE I', 15, 'NULL', 3, 1, 19, 30, NULL),
(286, 'IPE I', 17, 'NULL', 3, 1, 19, 30, NULL),
(287, 'IPE I', 7, 'NULL', 3, 1, 19, 30, NULL),
(288, 'IPE Ii', 8, 'NULL', 2, 1, 19, 30, NULL),
(289, 'IPE', 11, 'NULL', 3, 1, 19, 30, NULL),
(290, 'IPE Ii', 12, 'NULL', 2, 1, 19, 30, NULL),
(291, 'IPE', 9, 'NULL', 3, 1, 19, 30, NULL),
(292, 'IPE Ii', 10, 'NULL', 2, 1, 19, 30, NULL),
(293, 'COORDINACIÓN RIESGOS', 30, 'NULL', 2, 1, 19, 30, NULL),
(294, 'Inglés', 21, 'NULL', 2, 1, 6, 30, NULL),
(295, 'Inglés', 23, 'NULL', 2, 1, 6, 30, NULL),
(296, 'Inglés', 25, 'NULL', 2, 1, 6, 30, NULL),
(297, 'Inglés', 13, 'NULL', 2, 1, 6, 30, NULL),
(298, 'Inglés', 15, 'NULL', 2, 1, 6, 30, NULL),
(299, 'Inglés', 17, 'NULL', 2, 1, 6, 30, NULL),
(300, 'Inglés Técnico', 7, 'NULL', 2, 1, 6, 30, NULL),
(301, 'Inglés Técnico', 9, 'NULL', 2, 1, 6, 30, NULL),
(302, 'Inglés Técnico', 11, 'NULL', 2, 1, 6, 30, NULL),
(303, 'Op. Bas. Prod. Y mant. Plan. Y', 27, 'NULL', 5, 1, 20, 30, NULL),
(304, 'Trabajos de aprovechamientos f', 27, 'NULL', 7, 1, 20, 30, NULL),
(305, 'Recolección de productos fores', 27, 'NULL', 1, 1, 20, 30, NULL),
(306, 'Operaciones básicas para el ma', 27, 'NULL', 6, 1, 20, 30, NULL),
(307, 'Tutoría', 27, 'NULL', 1, 1, 20, 30, NULL),
(308, 'Operaciones básicas para el ma', 28, 'NULL', 5, 1, 20, 30, NULL),
(309, 'Repoblación e infraestructura ', 28, 'NULL', 5, 1, 20, 30, NULL),
(310, 'Silvicultura y plagas', 28, 'NULL', 5, 1, 20, 30, NULL),
(311, 'Tutoría', 28, 'NULL', 1, 1, 20, 30, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `optativas`
--

CREATE TABLE `optativas` (
  `id` int(2) NOT NULL,
  `nombre` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

--
-- Volcado de datos para la tabla `optativas`
--

INSERT INTO `optativas` (`id`, `nombre`) VALUES
(4, 'Diver\n'),
(3, 'Diver y Grupo 3 (4 4º ESO)\n'),
(6, 'Grupo 10 y Diver\n'),
(5, 'Grupo 10 y Plur\n'),
(7, 'Grupo 6\n'),
(8, 'Grupo 7\n'),
(9, 'Grupo 8\n'),
(10, 'Grupo 9'),
(1, 'No ofertada\n'),
(2, 'Plurilingüe\n');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_asignatura`
--

CREATE TABLE `tipo_asignatura` (
  `id` int(2) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `clave_tipo` varchar(2) DEFAULT NULL,
  `añadir` int(11) NOT NULL,
  `factor` decimal(2,1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

--
-- Volcado de datos para la tabla `tipo_asignatura`
--

INSERT INTO `tipo_asignatura` (`id`, `nombre`, `clave_tipo`, `añadir`, `factor`) VALUES
(1, 'Normal', 'N', 0, 1.0),
(2, 'Plurilingüe', 'PL', 1, 1.0),
(3, 'Optativa', 'OP', 0, 0.5),
(4, 'Pluri/Opta', 'PO', 1, 0.5),
(5, 'Diversificación', 'DV', -2, 1.0),
(6, 'Especial', 'ES', -3, 1.0),
(7, 'Bach. Opt. 1', 'B1', 1, 0.0),
(8, 'Bach. Opt. 2', 'B2', 2, 0.0),
(9, 'Bach. Opt. 3', 'B3', 3, 0.0),
(10, 'Bach. Opt. 4', 'B4', 4, 0.0),
(11, 'Bach. Opt. 5', 'B5', 5, 0.0),
(12, 'PluriDiver', 'PV', 2, 1.0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `turnos`
--

CREATE TABLE `turnos` (
  `id` int(1) NOT NULL,
  `nombre` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

--
-- Volcado de datos para la tabla `turnos`
--

INSERT INTO `turnos` (`id`, `nombre`) VALUES
(1, 'M\n'),
(4, 'MT\n'),
(7, 'MTV'),
(5, 'MV\n'),
(2, 'T\n'),
(6, 'TV\n'),
(3, 'V\n');

-- --------------------------------------------------------

--
-- Estructura Stand-in para la vista `vista_horas_departamentos`
-- (Véase abajo para la vista actual)
--
CREATE TABLE `vista_horas_departamentos` (
`departamento` varchar(30)
,`1º ESO` decimal(44,0)
,`2ª ESO` decimal(44,0)
,`3º ESO` decimal(44,0)
,`4º ESO` decimal(44,0)
,`1º Bachilerato` decimal(44,0)
,`2º Bachillerato` decimal(44,0)
,`1º GB Admon` decimal(44,0)
,`1º GB Forestal` decimal(44,0)
,`1º GM ACOM` decimal(44,0)
,`1º GM ADTVA` decimal(44,0)
,`1º GM SMR` decimal(44,0)
,`1º GS AFI` decimal(44,0)
,`1º GS ASD` decimal(44,0)
,`1º GS ASIR` decimal(44,0)
,`1º GS DAM` decimal(44,0)
,`1º GSCINT` decimal(44,0)
,`1º GSTYL` decimal(44,0)
,`2º GB Admon` decimal(44,0)
,`2º GB Forestal` decimal(44,0)
,`2º GM ACOM` decimal(44,0)
,`2º GM ADTVA` decimal(44,0)
,`2º GM SMR` decimal(44,0)
,`2º GS AFI` decimal(44,0)
,`2º GS ASD` decimal(44,0)
,`2º GS ASIR` decimal(44,0)
,`2º GS DAM` decimal(44,0)
,`2º GSCINT` decimal(44,0)
,`2º GSTYL` decimal(44,0)
,`Varios` decimal(44,0)
,`Total` decimal(44,0)
);

-- --------------------------------------------------------

--
-- Estructura Stand-in para la vista `vista_materias_cursos`
-- (Véase abajo para la vista actual)
--
CREATE TABLE `vista_materias_cursos` (
`id` int(2)
,`materia` varchar(30)
,`grupo` varchar(20)
,`horas_semanales` int(2)
,`curso` varchar(20)
,`tipo` varchar(20)
,`departamento` varchar(30)
,`especialidad` int(2)
,`horas_totales` decimal(22,0)
);

-- --------------------------------------------------------

--
-- Estructura para la vista `vista_horas_departamentos`
--
DROP TABLE IF EXISTS `vista_horas_departamentos`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vista_horas_departamentos`  AS SELECT `vista_materias_cursos`.`departamento` AS `departamento`, sum(if(`vista_materias_cursos`.`curso` = '1º ESO',`vista_materias_cursos`.`horas_totales`,0)) AS `1º ESO`, sum(if(`vista_materias_cursos`.`curso` = '2ª ESO',`vista_materias_cursos`.`horas_totales`,0)) AS `2ª ESO`, sum(if(`vista_materias_cursos`.`curso` = '3º ESO',`vista_materias_cursos`.`horas_totales`,0)) AS `3º ESO`, sum(if(`vista_materias_cursos`.`curso` = '4º ESO',`vista_materias_cursos`.`horas_totales`,0)) AS `4º ESO`, sum(if(`vista_materias_cursos`.`curso` = '1º Bachilerato',`vista_materias_cursos`.`horas_totales`,0)) AS `1º Bachilerato`, sum(if(`vista_materias_cursos`.`curso` = '2º Bachillerato',`vista_materias_cursos`.`horas_totales`,0)) AS `2º Bachillerato`, sum(if(`vista_materias_cursos`.`curso` = '1º GB Admon',`vista_materias_cursos`.`horas_totales`,0)) AS `1º GB Admon`, sum(if(`vista_materias_cursos`.`curso` = '1º GB Forestal',`vista_materias_cursos`.`horas_totales`,0)) AS `1º GB Forestal`, sum(if(`vista_materias_cursos`.`curso` = '1º GM ACOM',`vista_materias_cursos`.`horas_totales`,0)) AS `1º GM ACOM`, sum(if(`vista_materias_cursos`.`curso` = '1º GM ADTVA',`vista_materias_cursos`.`horas_totales`,0)) AS `1º GM ADTVA`, sum(if(`vista_materias_cursos`.`curso` = '1º GM SMR',`vista_materias_cursos`.`horas_totales`,0)) AS `1º GM SMR`, sum(if(`vista_materias_cursos`.`curso` = '1º GS AFI',`vista_materias_cursos`.`horas_totales`,0)) AS `1º GS AFI`, sum(if(`vista_materias_cursos`.`curso` = '1º GS ASD',`vista_materias_cursos`.`horas_totales`,0)) AS `1º GS ASD`, sum(if(`vista_materias_cursos`.`curso` = '1º GS ASIR',`vista_materias_cursos`.`horas_totales`,0)) AS `1º GS ASIR`, sum(if(`vista_materias_cursos`.`curso` = '1º GS DAM',`vista_materias_cursos`.`horas_totales`,0)) AS `1º GS DAM`, sum(if(`vista_materias_cursos`.`curso` = '1º GSCINT',`vista_materias_cursos`.`horas_totales`,0)) AS `1º GSCINT`, sum(if(`vista_materias_cursos`.`curso` = '1º GSTYL',`vista_materias_cursos`.`horas_totales`,0)) AS `1º GSTYL`, sum(if(`vista_materias_cursos`.`curso` = '2º GB Admon',`vista_materias_cursos`.`horas_totales`,0)) AS `2º GB Admon`, sum(if(`vista_materias_cursos`.`curso` = '2º GB Forestal',`vista_materias_cursos`.`horas_totales`,0)) AS `2º GB Forestal`, sum(if(`vista_materias_cursos`.`curso` = '2º GM ACOM',`vista_materias_cursos`.`horas_totales`,0)) AS `2º GM ACOM`, sum(if(`vista_materias_cursos`.`curso` = '2º GM ADTVA',`vista_materias_cursos`.`horas_totales`,0)) AS `2º GM ADTVA`, sum(if(`vista_materias_cursos`.`curso` = '2º GM SMR',`vista_materias_cursos`.`horas_totales`,0)) AS `2º GM SMR`, sum(if(`vista_materias_cursos`.`curso` = '2º GS AFI',`vista_materias_cursos`.`horas_totales`,0)) AS `2º GS AFI`, sum(if(`vista_materias_cursos`.`curso` = '2º GS ASD',`vista_materias_cursos`.`horas_totales`,0)) AS `2º GS ASD`, sum(if(`vista_materias_cursos`.`curso` = '2º GS ASIR',`vista_materias_cursos`.`horas_totales`,0)) AS `2º GS ASIR`, sum(if(`vista_materias_cursos`.`curso` = '2º GS DAM',`vista_materias_cursos`.`horas_totales`,0)) AS `2º GS DAM`, sum(if(`vista_materias_cursos`.`curso` = '2º GSCINT',`vista_materias_cursos`.`horas_totales`,0)) AS `2º GSCINT`, sum(if(`vista_materias_cursos`.`curso` = '2º GSTYL',`vista_materias_cursos`.`horas_totales`,0)) AS `2º GSTYL`, sum(if(`vista_materias_cursos`.`curso` = 'Varios',`vista_materias_cursos`.`horas_totales`,0)) AS `Varios`, sum(`vista_materias_cursos`.`horas_totales`) AS `Total` FROM `vista_materias_cursos` GROUP BY `vista_materias_cursos`.`departamento` ;

-- --------------------------------------------------------

--
-- Estructura para la vista `vista_materias_cursos`
--
DROP TABLE IF EXISTS `vista_materias_cursos`;

CREATE ALGORITHM=TEMPTABLE DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vista_materias_cursos`  AS SELECT `m`.`id` AS `id`, `m`.`nombre` AS `materia`, `m`.`grupo` AS `grupo`, `m`.`horas_semanales` AS `horas_semanales`, `c`.`nombre` AS `curso`, `ta`.`nombre` AS `tipo`, `d`.`nombre` AS `departamento`, `e`.`id` AS `especialidad`, `m`.`horas_semanales`* truncate(`c`.`grupos` * `ta`.`factor`,0) + `ta`.`añadir` AS `horas_totales` FROM ((((`materias` `m` join `cursos` `c` on(`m`.`id_curso` = `c`.`id`)) join `tipo_asignatura` `ta` on(`m`.`id_tipo` = `ta`.`id`)) left join `departamentos` `d` on(`m`.`id_departamento` = `d`.`id`)) left join `especialidades` `e` on(`m`.`id_especialidad` = `e`.`id`)) ;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cursos`
--
ALTER TABLE `cursos`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`),
  ADD KEY `fk_turnos` (`turnos`);

--
-- Indices de la tabla `departamentos`
--
ALTER TABLE `departamentos`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `clave_dpto` (`clave_dpto`);

--
-- Indices de la tabla `especialidades`
--
ALTER TABLE `especialidades`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `materias`
--
ALTER TABLE `materias`
  ADD PRIMARY KEY (`id`,`id_curso`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `fk_id_curso` (`id_curso`),
  ADD KEY `fk_id_tipo` (`id_tipo`),
  ADD KEY `fk_id_departamento` (`id_departamento`),
  ADD KEY `fk_id_especialidad` (`id_especialidad`),
  ADD KEY `fk_id_optativa` (`id_optativa`);

--
-- Indices de la tabla `optativas`
--
ALTER TABLE `optativas`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `tipo_asignatura`
--
ALTER TABLE `tipo_asignatura`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`),
  ADD UNIQUE KEY `clave_tipo` (`clave_tipo`);

--
-- Indices de la tabla `turnos`
--
ALTER TABLE `turnos`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `cursos`
--
ALTER TABLE `cursos`
  ADD CONSTRAINT `fk_turnos` FOREIGN KEY (`turnos`) REFERENCES `turnos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `materias`
--
ALTER TABLE `materias`
  ADD CONSTRAINT `fk_id_curso` FOREIGN KEY (`id_curso`) REFERENCES `cursos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_id_departamento` FOREIGN KEY (`id_departamento`) REFERENCES `departamentos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_id_especialidad` FOREIGN KEY (`id_especialidad`) REFERENCES `especialidades` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_id_optativa` FOREIGN KEY (`id_optativa`) REFERENCES `optativas` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_id_tipo` FOREIGN KEY (`id_tipo`) REFERENCES `tipo_asignatura` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
