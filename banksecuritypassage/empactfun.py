#Employee Action Log
import mysql.connector
from BankSecurityPassage import manver
#Creating cursor for sql
db = 
mysql.connector.connect(host="localhost",user="root",passwd="Sonit@123",d
atabase="scb_bank")
curs=db.cursor()
def empactfunw(empds,empname,dt,act):
 exst="INSERT INTO emplact values 
("+empds+','+empname+','+dt+','+act+")"
 curs.execute(exst)
 db.commit()
def empactfunr(empcds):
 curs.execute("select * from emplact where empcode="+empcds)
 log=curs.fetchall()
 for i in log:
 print("Date: ",i[2])
 print("Action: ",i[3])
 print()

