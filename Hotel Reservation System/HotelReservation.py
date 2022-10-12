

#Python Module:Payroll Management


import Module1
import Module2
import Module3
import Module4
import Module5
import Module6
import Module7



while True:
    print("\t\t******Hotel Reservation System******\n")
    print("==========================================")
    print("1. To Add New Record")
    print("2. To Search a Record")
    print("3. To Update the Records")
    print("4. To Delete the Record")
    print("5. To View All the Record")
    print("6. To Generate the Report")
    print("7. Database Setup")
    print("8. Exit")
    print("==========================================")
    choice=int(input("Enter choice between 1 to 8 -------> :"))
    if choice==1:
        Module1.AddRecord()
    elif choice==2:
        Module2.SearchRecord()
    elif choice==3:
        Module3.UpdateRecord()
    elif choice==4:
        Module4.DeleteRecord()
    elif choice==5:
        Module5.DisplayRecord()
    elif choice==6:
        Module6.GenerateReport()
    elif choice==7:
        Module7.DataBase()
    elif choice==8:
        break
    else:
        print("Wrong choice.......Enter your choice again")
        x=input("Enter any key to continue")
