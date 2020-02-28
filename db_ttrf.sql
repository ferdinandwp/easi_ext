-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: db_ttrf
-- ------------------------------------------------------
-- Server version	8.0.19

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
-- Table structure for table `ttrf`
--

DROP TABLE IF EXISTS `ttrf`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ttrf` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tech_owner` varchar(100) DEFAULT NULL,
  `owner_contact` varchar(100) DEFAULT NULL,
  `data_recipient` varchar(100) DEFAULT NULL,
  `recipient_location` varchar(100) DEFAULT NULL,
  `is_final_dst` tinyint(1) DEFAULT NULL,
  `final_dst` varchar(100) DEFAULT NULL,
  `export_requester` varchar(100) DEFAULT NULL,
  `date_req` date DEFAULT NULL,
  `method_export` varchar(100) DEFAULT NULL,
  `purpose_export` varchar(100) DEFAULT NULL,
  `ip_owner` varchar(100) DEFAULT NULL,
  `tech_describe` longtext,
  `ecl` varchar(100) DEFAULT NULL,
  `eccn` varchar(100) DEFAULT NULL,
  `usml` varchar(100) DEFAULT NULL,
  `cg` varchar(100) DEFAULT NULL,
  `sme_decision` tinyint(1) DEFAULT NULL,
  `sme_reason` varchar(100) DEFAULT NULL,
  `sme_name` varchar(100) DEFAULT NULL,
  `sme_decision_date` date DEFAULT NULL,
  `ecm_decision` tinyint(1) DEFAULT NULL,
  `ecm_reason` varchar(100) DEFAULT NULL,
  `ecm_name` varchar(100) DEFAULT NULL,
  `ecm_decision_date` date DEFAULT NULL,
  `ecm_license_req` tinyint(1) DEFAULT NULL,
  `ecm_license_no` varchar(100) DEFAULT NULL,
  `ecm_license_expiry_date` date DEFAULT NULL,
  `date_ini_export` date DEFAULT NULL,
  `export_recipient` varchar(100) DEFAULT NULL,
  `method_transfer` varchar(100) DEFAULT NULL,
  `exported_by` varchar(100) DEFAULT NULL,
  `export_is_completed` tinyint(1) DEFAULT NULL,
  `record_num` int DEFAULT NULL,
  `uploaded_file` mediumblob,
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ttrf`
--

LOCK TABLES `ttrf` WRITE;
/*!40000 ALTER TABLE `ttrf` DISABLE KEYS */;
/*!40000 ALTER TABLE `ttrf` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-02-27 15:50:23
