from sqlite4 import SQLite4


def create_table():
    database = SQLite4("database.db")
    try:
        database.connect()
        query = "CREATE TABLE employee (id INTEGER PRIMARY KEY, name VARCHAR, post VARCHAR, salary VARCHAR)"
        result = database.execute(query)
    except :
        print("database connection failed")