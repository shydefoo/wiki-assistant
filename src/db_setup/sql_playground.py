from db_setup import load_sql_scripts
from db_setup.DBConnect import DBConnect


dbInstance = DBConnect()
cursor = dbInstance.db_connection.cursor()
def check_tables():
    cursor.execute("SHOW TABLES IN wiki_database")
    for table in cursor:
        print(table)

def create_test_db():
    cursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")


if __name__ == "__main__":
    create_test_db()
    check_tables()




