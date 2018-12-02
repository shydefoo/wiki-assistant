from flask_table import Table, Col
from db_setup.DBConnect import DBConnect
from utils.wiki_logger import WikiLogger


class ServiceBase:

    def __init__(self, name=__name__):
        self.db_instance = DBConnect()
        self.logger = WikiLogger(name).logger

    def get_result(self, *args, **kwargs):
        raise NotImplementedError

    def helper(self, item):
        output = []
        for x in item:
            if isinstance(x, bytearray):
                x = str(x, 'utf-8')
            output.append(x)
        return output

    def build_table(self, result, field_names):

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
        item_table = ItemTable(result)

        return item_table