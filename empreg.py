
#Employee Registration Module
import mysql.connector
from BankSecurityPassage import manver
#Creating cursor for sql
db = mysql.connector.connect(host="localhost",user="root",passwd="Sonit@123",database="scb_bank")
curs=db.cursor()
def empregfun():
 print("Enter Manager Master Code to Proceed:",end="")
 mmcd=input()
 if manver.manverfun(mmcd) == "Manager Verified!":
 print(manver.manverfun(mmcd))
 i=10001
 empcd=0
 while (i>10000):
 exst="select * from emplist where code="+str(i)
 curs.execute(exst)
 tempcd=curs.fetchone()
 if tempcd==None:
 empcd=i
 print("Enter Employee Name:",end="")
 nm=input()
 nm="\'"+nm+"\'"
 pas=input("Allot a password to employee:")
 est="insert into emplist values ("+str(empcd)+','+nm+','+pas+")"
 curs.execute(est)
Page | 13
 db.commit()
 print()
 print("Employee Added Sucessfully!")
 
 break
 else:
 i+=1
 pass
 elif manver.manverfun(mmcd) == "Incorrect Password....." :
 print("Incorrect Master Password. Exiting....")
 
 exit()
