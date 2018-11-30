import os

CURRENT_DIR = os.path.dirname(os.path.realpath(__name__))
HOME = os.path.dirname(os.path.dirname(CURRENT_DIR))
DATA_DIR = os.path.join(HOME, 'data')
TABLE_SETUP = os.path.join(CURRENT_DIR, 'table_setup')


PAGE = 'simplewiki-20181120-page.sql'
PAGE_PROPS = 'simplewiki-20181120-page_props.sql'
CREATE_PAGE_TABLE = 'create_pages_table.sql'

def read_sql_script(pathname):
    with open(os.path.join(DATA_DIR,pathname)) as file:
        sql_script = file.read()
    return sql_script

def create_page_table():
    with open(os.path.join(TABLE_SETUP, CREATE_PAGE_TABLE)) as file:
        query = file.read()
        print(query)
        return query


if __name__ == '__main__':
    create_page_table()


