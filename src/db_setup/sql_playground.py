from db_setup import load_sql_scripts
from db_setup.DBConnect import DBConnect


dbInstance = DBConnect()

def check_tables():
    dbInstance.cursor.execute("SHOW TABLES IN wiki_database")
    for table in dbInstance.cursor:
        print(table)

def create_test_db():
    dbInstance.cursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")


if __name__ == "__main__":
    # load_sql_scripts.create_tables()
    # create_test_db()
    # load_sql_scripts.load_data()
    # check_tables()
    load_sql_scripts.run_sql_file()




