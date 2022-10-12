#Python Module: Module4


from datetime import date,datetime,timedelta
import mysql.connector


def UpdateRecord():
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="Hotel")
        mycursor=mydb.cursor()
        cust_id=int(input("Enter Customer ID to be Updated: "))
        sql="select * from CustomerDetail where cust_id=%s"
        val=(cust_id,)
        print("Enter New Record")
        #cust_id=int(input("Enter the Customer ID: "))
        cust_name=input("Enter the Customer Name: ")
        address=input("Enter the Address: ")
        roomno=int(input("Enter the Room Number: "))
        mobileno=input("Enter the Mobile Number: ")
        check_in=input("Enter the Check-In Date (YYYY-MM-DD): ")
        check_out=input("Enter the Check-Out Date (YYYY-MM-DD): ")
        adv_payment=float(input("Enter the Advance Amount: "))
        room_type=input("Room Type:- \n 1. Suite (Rs. 2000 /day) \n 2. Delux (Rs. 1000 /day) \n 3. Standard (Rs. 500 /day): ")
        sql2="update CustomerDetail set cust_name=%s,address=%s,roomno=%s,mobileno=%s,check_in=%s,check_out=%s,adv_payment=%s,room_type=%s where cust_id=%s"
        val2=(cust_name,address,roomno,mobileno,check_in,check_out,adv_payment,room_type,cust_id)
        mycursor.execute(sql2,val2)
        mydb.commit()
        mycursor.close()
        mydb.close()
        print("Records Updated Successfully..........")

    except Exception as ex:
        print("Something went wrong",ex)
        
    mydb.close()

