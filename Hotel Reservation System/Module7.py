import MyDatabase

def DataBase():
    while True:
        print("\t\t*****Database Management*****\n")
        print("=====================================")
        print("1. Database Creation")
        print("2. Creation of Relations")
        print("3. List of Relations")
        print("4. Return to Main Menu")
        print("======================================")
        choice=int(input("Enter choice between 1 to 4-------->: "))
        if choice==1:
            MyDatabase.CreateDatabase()
        elif choice==2:
            MyDatabase.CreateRelations()
        elif choice==3:
            MyDatabase.ShowRelations()
        elif choice==4:
            return
        else:
            print("Wrong choice.......Enter your choice again")
            x=input("Enter any key to continue")
