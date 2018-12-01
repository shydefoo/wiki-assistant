import os
from db_setup.DBConnect import DBConnect
from utils.sql_file_parser import parse_sql
from utils.wiki_logger import WikiLogger

logger = WikiLogger().logger

CURRENT_DIR = os.path.dirname(os.path.realpath(__name__))
HOME = os.path.dirname(os.path.dirname(CURRENT_DIR))
DATA_DIR = os.path.join(HOME, 'data')
TABLE_SETUP = os.path.join(CURRENT_DIR, 'table_setup')


PAGE = 'simplewiki-20181120-page.sql'
PAGE_PROPS = 'simplewiki-20181120-page_props.sql'
CAT_LINKS = 'simplewiki-20181120-categorylinks.sql'
PAGE_LINKS = 'simplewiki-20181120-pagelinks.sql'
CAT = 'simplewiki-20181120-category.sql'
CHANGE_LOGS = 'simplewiki-20181120-change_tag.sql'
REVISION = 'simplewiki-20181120-revision.sql'


CREATE_PAGE_TABLE = 'create_pages_table.sql'
CREATE_CAT_TABLE = 'create_category_table.sql'
CREATE_CAT_LINKS_TABLE = 'create_category_links.sql'
CREATE_PAGELINKS_TABLE = 'create_pagelinks_table.sql'
CREATE_REVISION_TABLE = 'create_revision_table.sql'

db_instance = DBConnect()


def read_sql_script(pathname):
    with open(os.path.join(DATA_DIR,pathname)) as file:
        sql_script = file.read()
    return sql_script


# helper function loads query from db_setup/table_setup
def load_create_query(create_file):
    print("loading file: {}".format(create_file))
    with open(os.path.join(TABLE_SETUP, create_file), 'r') as file:
        query = file.read()
    #print("query: {}".format(query))
    return query


def run_sql_file(input_file, file_dir):
    filename = os.path.join(file_dir, input_file)
    stmts = parse_sql(filename)
    for stmt in stmts:
        db_instance.cursor.execute(stmt)
        logger.info("{} loaded".format(filename))
        logger.debug("{} ".format(stmt))
        db_instance.db_connection.commit()

def create_tables():
    filenames = [CREATE_PAGE_TABLE, CREATE_PAGELINKS_TABLE, CREATE_CAT_LINKS_TABLE, CREATE_CAT_TABLE]
    for file in filenames:
        run_sql_file(file, TABLE_SETUP)

def load_data():
    file_list = [PAGE, PAGE_LINKS, CAT, CAT_LINKS]
    #file_list = [CAT]
    for file in file_list:
        run_sql_file(file, DATA_DIR)


def convert_xml_to_sql(input_file):
    pass



if __name__ == '__main__':
    # run_sql_file(CREATE_PAGE_TABLE, TABLE_SETUP)
    # run_sql_file(PAGE, DATA_DIR)
    # run_sql_file(CREATE_CAT_TABLE, TABLE_SETUP)
    # run_sql_file(CREATE_PAGELINKS_TABLE, TABLE_SETUP)
    # run_sql_file(CREATE_PAGELINKS_TABLE, TABLE_SETUP)
    run_sql_file(CREATE_REVISION_TABLE, TABLE_SETUP)
    run_sql_file(REVISION, DATA_DIR)

