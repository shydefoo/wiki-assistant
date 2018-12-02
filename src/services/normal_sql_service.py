from services.service_base_class import ServiceBase
from utils.sql_timer import time_query
from utils.wiki_logger import WikiLogger


class ExecuteQuery(ServiceBase):
    name = 'ExecuteQuery'
    def __init__(self):
        super(ExecuteQuery, self).__init__(self.name)

    def get_result(self, query):
        try:
            val, time = self.execute_sql_query(query)
            result = val[0]
            field_names = val[1]
            self.logger.debug("result: {}, field_names: {}, time: {}".format(result, field_names, time))
            if isinstance(result, list):
                table = self.build_table(result, field_names)
                return table.__html__(), time
            else:
                self.logger.info("Invalid query")
                return "Error", "Error"
        except:
            raise Exception


    @time_query
    def execute_sql_query(self, query):
        self.logger.info("Query: {}".format(query))
        try:
            cursor = self.db_instance.db_connection.cursor()
            cursor.execute(query)
            field_names = [i[0] for i in cursor.description]
            result = list(map(self.helper, cursor.fetchall()))
            return result, field_names
        except Exception as e:
            self.logger.error(e)
            return 'Error processing sql code: {}'.format(e)


# logger = WikiLogger(__name__).logger
#
#
# def get_results(query):
#     val, time = execute_sql_query(query)
#     result = val[0]
#     field_names = val[1]
#     print(time)
#     if isinstance(result, list):
#         table = build_table(result, field_names)
#         return table.__html__(), time
#     else:
#         print(type(result))
#         return "error"
#
# def _helper(item):
#     output = []
#     for x in item:
#         if isinstance(x, bytearray):
#             x = str(x, 'utf-8')
#         output.append(x)
#     return output
#
# @time_query
# def execute_sql_query(query):
#
#     db_instance = DBConnect()
#     logger.info("Query: {}".format(query))
#     try:
#         db_instance.cursor.execute(query)
#         field_names = [i[0] for i in db_instance.cursor.description]
#         result = list(map(_helper, db_instance.cursor.fetchall()))
#         return result, field_names
#     except Exception as e:
#         logger.error(e)
#         return 'Error processing sql code: {}'.format(e)
#
#
#
# def build_table(result, field_names):
#
#     class_name = 'ItemTable'
#     base = (Table,)
#     attr = {}
#     for name in field_names:
#         attr[name] = Col(name)
#
#     ItemTable = type(class_name, base, attr)
#     def _build_item_dict(row):
#         item_dict = {}
#         for field, row_val in zip(field_names, row):
#             item_dict[field] = row_val
#         return item_dict
#     result = list(map(_build_item_dict, result))
#     item_table = ItemTable(result)
#
#     return item_table

if __name__ == '__main__':
    query = 'SELECT * FROM category LIMIT 100;'
    result = get_results(query)
    print(result)

