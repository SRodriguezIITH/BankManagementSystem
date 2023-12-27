#Employee Verification Module

import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='Sonit@123',database='scb_bank')
curs=mydb.cursor() #Creating a MySQl cursor object

def empverfun(empcd,pas):  #defined function returning a string
 k="Select Pass from emplist where Code="+str(empcd)
 curs.execute(k)
 r=curs.fetchone()

#The following condiionals check if the employee password exists and correct in the MySQL database table or not
 if r==None:
 res=("Employee Does Not Exist. Exiting...")
 quit() 
 elif (r[0])!=pas:
 res=("Incorrect Password.....")
 elif (r[0])==pas:
 res=("Employee Verified!")
 return res
