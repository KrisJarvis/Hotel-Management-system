#Python Module: Module1


from datetime import date,datetime,timedelta
import mysql.connector



def AddRecord():
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="Hotel")
        mycursor=mydb.cursor()
        print("Enter Customer's information......")
        cust_id=int(input("Enter the Customer ID: "))
        cust_name=input("Enter the Customer Name: ")
        address=input("Enter the Address: ")
        roomno=int(input("Enter the Room Number: "))
        mobileno=input("Enter the Mobile Number: ")
        check_in=input("Enter the Check-In Date (YYYY-MM-DD): ")
        check_out=input("Enter the Check-Out Date (YYYY-MM-DD): ")
        adv_payment=float(input("Enter the Advance Amount: "))
        room_type=int(input("Room Type:- \n 1. Suite (Rs. 2000 /day) \n 2. Deluxe (Rs. 1000 /day) \n 3. Standard (Rs. 500 /day)\n"))
        
        if room_type==1:
            room_type="Suite"
        elif room_type==2:
            room_type="Deluxe"
        elif room_type==3:
            room_type="Standard"
        else:
            print("Enter the correct choice")
        #noofdays=" "
            
        sql="insert into CustomerDetail values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(cust_id,cust_name,address,roomno,mobileno,check_in,check_out,adv_payment,room_type)
        mycursor.execute(sql,val)
        mydb.commit()
        mycursor.close()
        mydb.close()
        print("Records Inserted Successfully..........")

    except Exception as ex:
        print("Something went wrong",ex)
        
    mydb.close()
