



#Python Module: Module6

from datetime import date
import datetime
import mysql.connector

def GenerateReport():
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="Hotel")
        mycursor=mydb.cursor()
        Tax=0.0
        cust_id=int(input("Enter the Customer ID: "))
        sql="select * from CustomerDetail where cust_id=%s"
        #val=(cust_id,)
        #mycursor.execute(sql,val)
        now=datetime.datetime.now()
        print("\n************THE TAJ HOTEL************\n")
        print("Current Date and Time: ",end=" ")
        print(now.strftime("%y-%m-%d %H:%M:%S"))
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
        print("check-in= ",check_in)
        print("check-out= ",check_out)

        ndays=check_out-check_in
        nofdays=ndays.days
        print("No of days= ",nofdays)
        print("===============================================")
        print("Hotel The Taj")
        print("500, North Extension")
        print("New Delhi")
        print("===============================================")
        print("Customer ID: ",cust_id)
        print("Customer Name: ",cust_name)
        print("Customer Address: ",address)
        print("===============================================")
        print("Room Number: ",roomno)
        print("Mobile Number: ",mobileno)
        print("===============================================")
        print("Check-In: ",check_in)
        print("Check-Out: ",check_out)
        print("Room Type: ",room_type)
        print("===============================================")
        print("Number of Days: ",ndays)

        if room_type=="Suite":
            price=2000
        elif room_type=="Deluxe":
            price=1000
        else:
            price=500

        Total=nofdays*price
        print("Total: ",Total)
        print("Advance: ",adv_payment)
        Tax=Total*0.10
        print("Tax: ",Tax)
        netamt=(float(Total)+float(Tax))-float(adv_payment)
        #net=float(adv_payment)-(float(Total)+float(Tax))
        #netamt=float(Total)+float(Tax)
        print("Net Amount: ",netamt)
        #print("Total Balance Payable to Customer: ",net)
            
        mydb.commit()
        mycursor.close()
        mydb.close()
        #print("Records Searched Successfully..........")

    except Exception as ex:
        print("Something went wrong",ex)
        
    mydb.close()
