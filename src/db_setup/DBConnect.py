import mysql.connector as connector
from utils.singleton import Singleton
from utils.wiki_logger import  WikiLogger
import os

HOST = os.getenv('HOST', '127.0.0.1')
USER = os.getenv('USERNAME', 'root')
DATABASE = os.getenv('TARGET_DB', 'wiki_database')
PORT = os.getenv('PORT_NUM', '3306')

# HOST = '127.0.0.1'
# USER = 'root'
# DATABASE = 'wiki_database'
# PORT = '3306'

logger = WikiLogger(__name__).logger

class DBConnect(metaclass=Singleton):

    def __init__(self):
        # temp way to init
        self.db_connection = connector.connect(user=USER, host=HOST, port=PORT, database=DATABASE, buffered=True)
        # self.cursor = self.db_connection.cursor()
        # logger.debug("DB connection set up")

    def __del__(self):
        # self.cursor.close()
        self.db_connection.close()


if __name__ == '__main__':
    db_instance = DBConnect()
    logger.debug(db_instance.db_connection)
