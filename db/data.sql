-- MySQL dump 10.13  Distrib 5.7.24, for osx10.9 (x86_64)
--
-- Host: localhost    Database: mydb2
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Algorithm`
--

DROP TABLE IF EXISTS `Algorithm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Algorithm` (
  `name` varchar(45) NOT NULL,
  `description` varchar(45) NOT NULL,
  `sourceUrl` varchar(256) NOT NULL,
  `date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Algorithm`
--

LOCK TABLES `Algorithm` WRITE;
/*!40000 ALTER TABLE `Algorithm` DISABLE KEYS */;
/*!40000 ALTER TABLE `Algorithm` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CleanedDataset`
--

DROP TABLE IF EXISTS `CleanedDataset`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CleanedDataset` (
  `id` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CleanedDataset`
--

LOCK TABLES `CleanedDataset` WRITE;
/*!40000 ALTER TABLE `CleanedDataset` DISABLE KEYS */;
/*!40000 ALTER TABLE `CleanedDataset` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `FaultRegistry`
--

DROP TABLE IF EXISTS `FaultRegistry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `FaultRegistry` (
  `id` int NOT NULL AUTO_INCREMENT,
  `detectionAlgorithm` varchar(45) NOT NULL,
  `faultyRecord` int NOT NULL COMMENT 'Identifies which record in the dataset has the fault',
  `sourceDatasetId` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UQ_SourceDetection` (`sourceDatasetId`, `detectionAlgorithm`), -- Added unique key constraint
  KEY `DetectionAlgorithmRef_idx` (`detectionAlgorithm`),
  KEY `SourceDatasetRef_idx` (`sourceDatasetId`),
  CONSTRAINT `DetectionAlgorithmRef` FOREIGN KEY (`detectionAlgorithm`) REFERENCES `Algorithm` (`name`),
  CONSTRAINT `SourceDatasetRef` FOREIGN KEY (`sourceDatasetId`) REFERENCES `SourceDataset` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FaultRegistry`
--

LOCK TABLES `FaultRegistry` WRITE;
/*!40000 ALTER TABLE `FaultRegistry` DISABLE KEYS */;
/*!40000 ALTER TABLE `FaultRegistry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Results`
--

DROP TABLE IF EXISTS `Results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Results` (
  `id` int NOT NULL,
  `executionIteration` int NOT NULL AUTO_INCREMENT COMMENT 'Analysis Iteration (Increments automatically doesn''t need to be added manually)',
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Analysis results release time',
  `recordNumberIncluded` bigint NOT NULL COMMENT 'Identifies how many record from the dataset where included in this analysis',
  `executedAlgorithm` varchar(45) NOT NULL,
  `datasetid` int NOT NULL,
  `faultRegistryid` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `execution_UNIQUE` (`executionIteration`),
  KEY `Algorithm_idx` (`executedAlgorithm`),
  KEY `DatasetReference_idx` (`datasetid`),
  KEY `FaultRegistryReference_idx` (`faultRegistryid`),
  CONSTRAINT `Algorithm` FOREIGN KEY (`executedAlgorithm`) REFERENCES `Algorithm` (`name`),
  CONSTRAINT `DatasetReference` FOREIGN KEY (`datasetid`) REFERENCES `SourceDataset` (`id`),
  CONSTRAINT `FaultRegistryReference` FOREIGN KEY (`faultRegistryid`) REFERENCES `FaultRegistry` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Results`
--

LOCK TABLES `Results` WRITE;
/*!40000 ALTER TABLE `Results` DISABLE KEYS */;
/*!40000 ALTER TABLE `Results` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SourceDataset`
--

DROP TABLE IF EXISTS `SourceDataset`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SourceDataset` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `file` varchar(45) DEFAULT NULL,
  `date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SourceDataset`
--

LOCK TABLES `SourceDataset` WRITE;
/*!40000 ALTER TABLE `SourceDataset` DISABLE KEYS */;
/*!40000 ALTER TABLE `SourceDataset` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-15 13:08:59
