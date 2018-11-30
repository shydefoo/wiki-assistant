from db_setup import load_sql_scripts
from db_setup.DBConnect import DBConnect


dbInstance = DBConnect()

def check_tables():
    dbInstance.cursor.execute("SHOW TABLES")
    for table in dbInstance.cursor:
        print(table)


if __name__ == "__main__":

    query = load_sql_scripts.create_page_table()
    dbInstance.cursor.execute(query, multi=True)
    # dbInstance.cursor.commit()

    check_tables()




