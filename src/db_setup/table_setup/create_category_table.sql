/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `category`
--

 DROP TABLE IF EXISTS `category`;
 /*!40101 SET @saved_cs_client     = @@character_set_client */;
 /*!40101 SET character_set_client = utf8 */;
 CREATE TABLE `category` (
   `cat_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
   `cat_title` varbinary(255) NOT NULL DEFAULT '',
   `cat_pages` int(11) NOT NULL DEFAULT '0',
   `cat_subcats` int(11) NOT NULL DEFAULT '0',
   `cat_files` int(11) NOT NULL DEFAULT '0',
   PRIMARY KEY (`cat_id`),
   UNIQUE KEY `cat_title` (`cat_title`),
   KEY `cat_pages` (`cat_pages`)
 ) ENGINE=InnoDB AUTO_INCREMENT=1501246 DEFAULT CHARSET=binary;
/*!40101 SET character_set_client = @saved_cs_client */;