
#Python Module: MyDatabase


from datetime import date,datetime,timedelta
import mysql.connector



def CreateDatabase():
       try:
              
              mydb=mysql.connector.connect(host="localhost",user="root",password="root")
              mycursor=mydb.cursor()
              print("Creating Hotel Database")
              sql="create database if not exists Hotel"
              mycursor.execute(sql)
              print("Hotel Database Created Successfully....")
              
       except Exception as ex:
              print(ex)
       


def CreateRelations():
       try:
              
              mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="Hotel")
              mycursor=mydb.cursor()
              print("Creating CustomerDetail Relation")
              sql="create table if not exists CustomerDetail(cust_id int primary key,cust_name varchar(50) not null,address varchar(450) not null,roomno int,mobileno char(10),check_in date,check_out date,adv_payment float,room_type varchar(50))"
              mycursor.execute(sql)
              print("CustomerDetail Relation Created Successfully....")

       except Exception as ex:
              print("Something went wrong",ex)


def ShowRelations():
       try:
              
              mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="Hotel")
              mycursor=mydb.cursor()
              print("Displaying List of Relations")
              sql="show tables"
              mycursor.execute(sql)
              for i in mycursor:
                     print(i)
               
       except Exception as ex:
              print("Something went wrong",ex)

       




