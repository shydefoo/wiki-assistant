import mysql.connector as connector
from utils.singleton import Singleton
from utils.wiki_logger import  WikiLogger
import os

HOST = os.getenv('HOST', '127.0.0.1')
USER = os.getenv('USERNAME', 'root')
DATABASE = os.getenv('TARGET_DB', 'wiki_database')
PW = os.getenv('MYSQL_ROOT_PASSWORD', '')
PORT = os.getenv('PORT_NUM', '3306')


logger = WikiLogger(__name__).logger

class DBConnect():

    def __init__(self):
        # temp way to init
        self.db_connection = connector.connect(user=USER, host=HOST, port=PORT, database=DATABASE, password=PW, buffered=True)
        # self.cursor = self.db_connection.cursor()
        # logger.debug("DB connection set up")
        self.db_connection.cursor().execute('SET GLOBAL max_allowed_packet=1073741824;')

    def __del__(self):
        # self.cursor.close()
        self.db_connection.close()

    def settings_for_sql_dump(self):
        cursor = self.db_connection.cursor()
        cursor.execute('set global net_buffer_length=1000000;')
        cursor.execute('set global net_buffer_length=1000000;')
        cursor.execute('SET AUTOCOMMIT = 0;')
        return cursor

if __name__ == '__main__':
    db_instance = DBConnect()
    logger.debug(db_instance.db_connection)
