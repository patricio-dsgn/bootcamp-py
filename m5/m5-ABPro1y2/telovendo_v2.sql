-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: telovendo
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `idclientes` int NOT NULL,
  `Nombre` varchar(45) NOT NULL,
  `Apellido` varchar(45) NOT NULL,
  `Telefono` varchar(20) NOT NULL,
  `Dirección` varchar(45) NOT NULL,
  `Comuna` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `FechaRegistro` date NOT NULL,
  `TotalPagado` int NOT NULL,
  PRIMARY KEY (`idclientes`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (5857694,'Manule','Campor','946446674','viana1255','Viña ','Manule@gmail.com','1964-03-03',340336),(6569192,'Jorge','Castro','959151737','limache 3405','Villa alemana','Jorge@gmail.com','1964-03-03',342375),(9921931,'Miguel','Tapia','986797404','alvarez 55','Quilpue','Miguel@gmail.com','1964-03-03',175199),(12289693,'Luis','Jara ','941998957','limache 3405','Viña ','Luis@gmail.com','1964-03-03',371133),(13902911,'Alonso','Jaramillo','965226693','viana1255','Quillota','Alonso@gmail.com','1964-03-03',76054),(15608269,'Claudio','Silva','928374756','peragallo 99','Viña ','Claudio@gmail.com','1964-03-03',362221),(15640021,'Pedro','Pascal','961240792','1 norte 580','Villa alemana','Pedro@gmail.com','1964-03-03',365128),(15966257,'Isaac','Benavides','964925545','alvarez 55','Quillota','Isaac@gmail.com','1964-03-03',49235),(17485284,'Jose','Balmaceda','909605427','peragallo 99','Valparaiso','Jose@gmail.com','1967-07-02',491616),(18784266,'Lorena','Morales','926899982','1 norte 580','Quilpue','Lorena@gmail.com','1964-03-03',383224);
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productos` (
  `SKU` int NOT NULL,
  `NombreProducto` varchar(45) NOT NULL,
  `Categoria` varchar(45) NOT NULL,
  `Fabricante` varchar(150) NOT NULL,
  `Stock` int NOT NULL,
  `Precio` int NOT NULL,
  PRIMARY KEY (`SKU`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` VALUES (1001,'Parlantes','electronica','Jbl',15,10000),(1002,'Notebook','computacion','HP',89,800000),(1003,'PC Gamer','computacion','Asus',20,1500000),(1004,'Swicht','computacion','Nintendo',60,350000),(1005,'Microondas','Linea Blana','Ursus Trotter',100,400000),(1006,'Teclado','Musica','Casio',32,150000),(1007,'Tijeras Poda','Jardin','Fitting',75,20000),(1008,'Living para Terraza','Terraza','Ikea',81,300000),(1009,'Cocina','Linea Blana','Madensa',4,200000),(1010,'Polera','Ropa Mujer','Zara',52,50000);
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vendedor`
--

DROP TABLE IF EXISTS `vendedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vendedor` (
  `Run` int NOT NULL,
  `NombreVendedor` varchar(45) NOT NULL,
  `ApellidosVendedor` varchar(45) NOT NULL,
  `FechaNacimiento` date NOT NULL,
  `Sección` varchar(45) NOT NULL,
  `salario` int NOT NULL,
  PRIMARY KEY (`Run`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vendedor`
--

LOCK TABLES `vendedor` WRITE;
/*!40000 ALTER TABLE `vendedor` DISABLE KEYS */;
INSERT INTO `vendedor` VALUES (1445753,'Diego','Velazquez','1988-10-17','Atención',1800000),(1545753,'Virginia','Lobos','1979-01-28','Ventas',193418),(1645753,'Juana','Cruz','1983-11-05','Ventas',1018659),(7598753,'Pedro','Paramo','1988-06-30','Bodega',838654),(8365753,'Vicente','Gomez','1990-07-21','Atención',1762730),(9543253,'Andrea','Pizarro','1968-05-23','Bodega',1414039),(10541453,'Guillemo','Blake','1982-08-14','Bodega',1465824),(11549853,'Angela','Davi','1976-04-25','Ventas',1617829),(12545753,'Luisa','Barrientos','1991-09-15','Bodega',577994),(130545753,'Gabriel','Garcia','1985-03-02','Bodega',1676392);
/*!40000 ALTER TABLE `vendedor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-25 21:54:08
