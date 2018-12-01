import mysql.connector as connector
from utils.singleton import Singleton
from utils.wiki_logger import  WikiLogger

HOST = '127.0.0.1'
USER = 'root'
DATABASE = 'wiki_database'
PORT = '3306'

logger = WikiLogger()

class DBConnect(metaclass=Singleton):

    def __init__(self):
        # temp way to init
        self.db_connection = connector.connect(user=USER, host=HOST, port=PORT, database=DATABASE)
        self.cursor = self.db_connection.cursor()
        # logger.debug("DB connection set up")

    def __del__(self):
        # self.cursor.close()
        self.db_connection.close()


if __name__ == '__main__':
    db_instance = DBConnect()
    print(db_instance.db_connection)
