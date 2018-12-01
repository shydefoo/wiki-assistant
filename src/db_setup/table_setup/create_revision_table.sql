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
 DROP TABLE IF EXISTS `revision`;
 /*!40101 SET @saved_cs_client     = @@character_set_client */;
 /*!40101 SET character_set_client = utf8 */;
 CREATE TABLE `revision`(
   `rev_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
   `rev_page` int(10) unsigned NOT NULL,
   `rev_text_id` int(10) unsigned NOT NULL,
   `rev_comment` varbinary(767) NOT NULL,
   `rev_user` int(10) unsigned NOT NULL DEFAULT '0',
   `rev_user_text` varbinary(255) NOT NULL,
   `rev_timestamp` varbinary(14) NOT NULL DEFAULT '0',
   `rev_minor_edit` tinyint(3) unsigned NOT NULL,
   `rev_deleted` tinyint(3) unsigned NOT NULL,
   `rev_len` int(10) unsigned DEFAULT NULL,
   `rev_parent_id` int(10) unsigned DEFAULT NULL,
   `rev_sha1` varbinary(32) NOT NULL,
   `rev_content_model` varbinary(32) DEFAULT NULL,
   `rev_content_format` varbinary(32) DEFAULT NULL,
    PRIMARY KEY (`rev_id`),
    UNIQUE KEY `rev_page_id` (`rev_page`, `rev_id`),
    KEY `rev_timestamp` (`rev_timestamp`),
    KEY `page_timestamp` (`rev_page`, `rev_timestamp`),
    KEY `user_timestamp` (`rev_user`, `rev_timestamp`),
    KEY `usertext_timestamp` (`rev_user_text`, `rev_timestamp`),
    KEY `page_user_timestamp` (`rev_page`, `rev_user`, `rev_timestamp`)
 ) ENGINE=InnoDB AUTO_INCREMENT=1501246 DEFAULT CHARSET=binary;
/*!40101 SET character_set_client = @saved_cs_client */;
