import db_init
import sqlite3

connection = sqlite3.connect("database.db")

def find_Employee(id):
    return connection.execute(f"SELECT * from employee where id={id}").fetchone()


def add_Employee():
    name = input("Enter Employee name: ")
    post = input("Enter Employee post: ")
    salary = input("Enter Employee salary: ")

    try:
        query = f"INSERT INTO employee (name, post, salary) VALUES ('{name}', '{post}', '{salary}');"
        connection.execute(query)   
        connection.commit()
        print("Employee was successfully created")
        menu()
    except:
        print("Something went wrong, try again later")
        menu()

def remove_Employee():
    try:
        id = int(input("Enter the Employee's id: "))
        emp = find_Employee(id)
        if emp is None:
            print("No Employee found!")
            raise
        query = f"DELETE from employee where id={id}"
        connection.execute(query)
        connection.commit()
        print("Employee was successfully deleted")
        menu()
    except:
        print("Something went wrong, try again later")
        menu()

def promote_Employee():
    try:
        id = int(input("Enter the Employee's id: "))
        emp = find_Employee(id)
        if emp is None:
            print("No Employee found!")
            raise
        promotion = input("Enter the Promotion: ")
        query = f"UPDATE employee SET post='{promotion}' WHERE id={id}"
        connection.execute(query)
        connection.commit()
        print("Employee was successfully updated")
        menu()
    except:
        print("Error")
        menu()

def display_one_Employee():
    try:
        id = int(input("Enter the Employee's id: "))
        emp = find_Employee(id)
        if emp is None:
            print("No Employee found!")
            raise
        print(emp)
        menu()
    except:
        print("Error")
        menu()


def display_all_Employees():
    emps = connection.execute("SELECT * FROM employee").fetchall()
    print("========== The Employee TABLE ==========")
    print("|  Id  |  Name  |  Post  |  Salary  |")
    print("----------------------------------------")
    for emp in emps:
        print(f"|  {emp[0]}  |  {emp[1]}  |  {emp[2]}  |  {emp[3]}  |")
    
    menu()

def menu():
    print("Welcome to Employee Managment Record")
    print("Press ")
    print("1 to Add Employee")
    print("2 to Remove Employee")
    print("3 to Promote Employee")
    print("4 to Display Employee")
    print("5 to Display All Employees")
    print("6 to Exit")

    try:
        ch = int(input("Enter your Choice: "))
        if ch == 1:
            add_Employee()
        elif ch == 2:
            remove_Employee()
        elif ch == 3:
            promote_Employee()
        elif ch == 4:
            display_one_Employee()
        elif ch == 5:
            display_all_Employees()
        elif ch == 6:
            pass
        else:
            raise
    except:
        print("++++++++++ invalid input +++++++++")
        menu()


db_init.create_table()
menu()
