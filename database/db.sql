-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         5.7.33 - MySQL Community Server (GPL)
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para itp
CREATE DATABASE IF NOT EXISTS `itp` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `itp`;

-- Volcando estructura para tabla itp.materias
CREATE TABLE IF NOT EXISTS `materias` (
  `id_materias` int(11) NOT NULL,
  `materia` varchar(50) NOT NULL,
  PRIMARY KEY (`id_materias`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla itp.materias: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `materias` DISABLE KEYS */;
INSERT IGNORE INTO `materias` (`id_materias`, `materia`) VALUES
	(1, 'Bases De Datos'),
	(2, 'Electronica Basica'),
	(3, 'Estadistica'),
	(4, 'Ingenieria De Software'),
	(5, 'Ingles II'),
	(6, 'Lenguajes Orientado A Objetos'),
	(7, 'Redes Y Comunicaciones');
/*!40000 ALTER TABLE `materias` ENABLE KEYS */;

-- Volcando estructura para tabla itp.rol
CREATE TABLE IF NOT EXISTS `rol` (
  `id_rol` int(11) NOT NULL,
  `tipo_rol` varchar(50) NOT NULL,
  PRIMARY KEY (`id_rol`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla itp.rol: ~2 rows (aproximadamente)
/*!40000 ALTER TABLE `rol` DISABLE KEYS */;
INSERT IGNORE INTO `rol` (`id_rol`, `tipo_rol`) VALUES
	(1, 'Estudiante'),
	(2, 'Profesor');
/*!40000 ALTER TABLE `rol` ENABLE KEYS */;

-- Volcando estructura para tabla itp.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombres` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `contraseña` varchar(50) DEFAULT NULL,
  `id_rol` int(3) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_rol` (`id_rol`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla itp.usuarios: ~2 rows (aproximadamente)
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT IGNORE INTO `usuarios` (`id`, `nombres`, `email`, `contraseña`, `id_rol`) VALUES
	(1, 'Administrador', 'admin', '123456789', 3),
	(9, 'Yilber Camilo Guevara', 'yilberg@yopmail.com', 'Camilo10*', 2),
	(19, 'Camilo', 'yilberg234@yopmail.com', 'Camilo10*', 1),
	(21, 'XD', 'yilberg324@yopmail.com', 'Camilo10*', 2),
	(22, 'Katerin Lineth', 'Katerin@hotmail.com', '12112016', 1);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
