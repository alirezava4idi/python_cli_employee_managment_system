import db_init

# db_init.create_table()

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
            pass
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

menu()
