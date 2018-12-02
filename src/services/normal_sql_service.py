from services.service_base_class import ServiceBase
from utils.sql_timer import time_query
from utils.wiki_logger import WikiLogger


class ExecuteQuery(ServiceBase):
    name = 'ExecuteQuery'
    def __init__(self):
        super(ExecuteQuery, self).__init__(self.name)

    def get_result(self, query):
        val, time = self.execute_sql_query(query)
        result = val[0]
        field_names = val[1]
        self.logger.debug("result: {}, field_names: {}, time: {}".format(result, field_names, time))
        if isinstance(result, list):
            table = self.build_table(result, field_names)
            return table.__html__(), self.insert_time(time)


    @time_query
    def execute_sql_query(self, query):
        self.logger.info("Query: {}".format(query))
        cursor = self.db_instance.db_connection.cursor()
        cursor.execute(query)
        field_names = [i[0] for i in cursor.description]
        result = list(map(self.helper, cursor.fetchall()))
        return result, field_names


