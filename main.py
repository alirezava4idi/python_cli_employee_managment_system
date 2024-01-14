import db_init
import sqlite3

connection = sqlite3.connect("database.db")


def add_Employee():
    name = input("Enter Employee name: ")
    post = input("Enter Employee post: ")
    salary = input("Enter Employee salary: ")

    try:
        query = f"INSERT INTO employee (name, post, salary) VALUES ('{name}', '{post}', '{salary}');"
        connection.execute(query)   
        connection.commit()
        print("Employee was successfully created")
    except:
        print("Something went wrong, try again later")

def remove_Employee():
    try:
        id = int(input("Enter the Employee's id: "))
        emp = connection.execute(f"SELECT * from employee where id={id}").fetchone()
        if emp is None:
            print("No Employee found!")
            raise
        query = f"DELETE from employee where id={id}"
        connection.execute(query)
        connection.commit()
        print("Employee was successfully deleted")
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
            remove_Employee()
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
