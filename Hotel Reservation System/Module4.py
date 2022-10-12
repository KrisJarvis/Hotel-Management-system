#Python Module: Module3


from datetime import date,datetime,timedelta
import mysql.connector



def DeleteRecord():
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="Hotel")
        mycursor=mydb.cursor()
        cust_id=int(input("Enter Customer ID to be Deleted: "))
        sql="delete from CustomerDetail where cust_id=%s"
        val=(cust_id,)
        mycursor.execute(sql,val)
        mydb.commit()
        mycursor.close()
        mydb.close()
        print("Records Deleted Successfully..........")

    except Exception as ex:
        print("Something went wrong",ex)
        
    mydb.close()
