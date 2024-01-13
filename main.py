import db_init
from sqlite4 import SQLite4


def add_Employee():
    name = input("Enter Employee name: ")
    post = input("Enter Employee post: ")
    salary = input("Enter Employee salary: ")

    database = SQLite4("database.db")
    try:
        database.connect()
        query = f"INSERT INTO employee (name, post, salary) VALUES ('{name}', '{post}', '{salary}');"
        database.execute(query)   
    except:
        print("Something went wrong, try again later")

def menu():
    print("Welcome to Employee Managment Record")
    print("Press ")
    print("1 to Add Employee")
    print("2 to Remove Employee")
    print("3 to Promote Employee")
    print("4 to Display Employee")
    print("5 to Exit")

    try:
        ch = int(input("Enter your Choice: "))
        if ch == 1:
            add_Employee()
        elif ch == 2:
            pass
        elif ch == 3:
            pass
        elif ch == 4:
            pass
        elif ch == 5:
            pass
        else:
            raise
    except:
        print("++++++++++ invalid input +++++++++")
        menu()


db_init.create_table()
menu()
