#Python Module: Module5


from datetime import date,datetime,timedelta
import mysql.connector

def SearchRecord():
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="Hotel")
        mycursor=mydb.cursor()
        cust_id=int(input("Enter Customer ID to be Searched: "))
        sql="select * from CustomerDetail where cust_id=%s"
        val=(cust_id,)
        mycursor.execute(sql,val)
        for (cust_id,cust_name,address,roomno,mobileno,check_in,check_out,adv_payment,room_type) in mycursor:
            print("==============================================")
            print("==============================================")
            print("Customer ID: ",cust_id)
            print("Customer Name: ",cust_name)
            print("Customer Address: ",address)
            print("Room Number: ",roomno)
            print("Mobile Number: ",mobileno)
            print("Check-In Date: ",check_in)
            print("Check-Out Date: ",check_out)
            print("Advance Payment:",adv_payment)
            print("Room Type:",room_type)
            print("===============================================")
        
        mydb.commit()
        mycursor.close()
        mydb.close()
        print("Record Searched Successfully..........")

    except Exception as ex:
        print("Something went wrong",ex)
        
    mydb.close()

