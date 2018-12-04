from db_setup.DBConnect import DBConnect
from services.service_base_class import ServiceBase
from utils.sql_file_parser import parse_sql
from utils.sql_timer import time_query
from utils.wiki_logger import WikiLogger
import os


CURRENT_DIR = os.path.dirname(__file__)
SQL_SCRIPTS_DIR = os.path.join(os.path.dirname(CURRENT_DIR), 'sql_scripts')
OUTDATEDNESS_SQL = os.path.join(SQL_SCRIPTS_DIR, 'outdatedness.sql')


class OutdatednessByCat(ServiceBase):
    name = 'OutdatednessByCat'

    def __init__(self):
        super(OutdatednessByCat, self).__init__(self.name)
        self.query = self.read_query(OUTDATEDNESS_SQL)

    def read_query(self, file):
        with open(file, 'r') as f:
            query = f.read()
        return query

    def get_result(self, category):

        val, time = self.execute_category_query(category)
        result = val[0]
        field_names = val[1]
        self.logger.debug("result: {}, field_names: {}, time: {}".format(result, field_names, time))
        if isinstance(result, list):
            table = self.build_table(result, field_names)
            return table.__html__(), self.insert_time(time)
        else:
            self.logger.info("Invalid query")
            return "Error", "Error"

    @time_query
    def execute_category_query(self, category):
        category = category.replace(' ', '_')
        cursor = self.db_instance.db_connection.cursor()
        cursor.execute(self.query, (category, category))
        field_names = [i[0] for i in cursor.description]
        result = list(map(self.helper, cursor.fetchall()))
        return result, field_names


