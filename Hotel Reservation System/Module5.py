#Python Module: Module5


from datetime import date,datetime,timedelta
import mysql.connector




def DisplayRecord():
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="Hotel")
        mycursor=mydb.cursor()
        sql="select * from CustomerDetail"
        mycursor.execute(sql)
        for (cust_id,cust_name,address,roomno,mobileno,check_in,check_out,adv_payment,room_type) in mycursor:
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

    except Exception as ex:
        print("Something went wrong",ex)
        
    mydb.close()
