from db_setup.DBConnect import DBConnect
from utils.wiki_logger import WikiLogger
from flask_table import Table, Col


logger = WikiLogger(__name__).logger


def get_results(query):
    result, field_names = execute_sql_query(query)
    if isinstance(result, list):
        table = build_table(result, field_names)
        return table.__html__()


def execute_sql_query(query):
    def _helper(item):
        output = []
        for x in item:
            if isinstance(x, bytearray):
                x = str(x, 'utf-8')
            output.append(x)
        return output

    db_instance = DBConnect()
    logger.info("Query: {}".format(query))
    try:
        db_instance.cursor.execute(query)
        field_names = [i[0] for i in db_instance.cursor.description]
        result = list(map(_helper, db_instance.cursor.fetchall()))
        return result, field_names
    except Exception as e:
        logger.error(e)
        return 'Error processing sql code: {}'.format(e)

def build_table(result, field_names):

    class_name = 'ItemTable'
    base = (Table,)
    attr = {}
    for name in field_names:
        attr[name] = Col(name)

    ItemTable = type(class_name, base, attr)
    def _build_item_dict(row):
        item_dict = {}
        for field, row_val in zip(field_names, row):
            item_dict[field] = row_val
        return item_dict
    result = list(map(_build_item_dict, result))
    print(result)
    item_table = ItemTable(result)

    return item_table

if __name__ == '__main__':
    query = 'SELECT * FROM category LIMIT 100;'
    result = get_results(query)
    print(result)

