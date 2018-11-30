import mysql.connector as connector
from utils.singleton import Singleton

HOST = '127.0.0.1'
USER = 'root'
DATABASE = 'wiki_database'

class DBConnect(metaclass=Singleton):
    def __init__(self):
        # temp way to init
        self.db_connection = connector.connect(user=USER, host=HOST, database=DATABASE)
        self.cursor = self.db_connection.cursor()

    def __del__(self):
        # self.cursor.close()
        self.db_connection.close()
