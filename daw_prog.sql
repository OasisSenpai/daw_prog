-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 18-05-2025 a las 18:32:21
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
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
