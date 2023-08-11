#Importing Modules
import time #To create time delay for user inertface and experience UI/UX
import datetime #To get real time systems date and time
#Importing from self created module
from BankSecurityPassage import empver,manver,empreg,empactfun,autopdf,loadf
import emoji #To print emoticons 
import pickle #Binary File Handling
import mysql.connector #To interface sql and python
from fpdf import FPDF #To create pdf based on given data
import random #To generate Random Number
#Generating a random integer for server request code
global rand
rand = random.randint(1000,100000)
#Creating cursor for sql
db=mysql.connector.connect(host="localhost",user="root",passwd="Sonit@123",
database="scb_bank")
curs=db.cursor()
#Creating object for datetime
todaytm=datetime.datetime.now()
#Printing Bank Name with logo(using Emoji Module)
print()
print(" "*39,emoji.emojize(":sunflower:")," Sunrise Chartered Bank SystemPortal",emoji.emojize(":bank:"))
print(" "*45,todaytm)
print()
Page | 18
#Function Manager which can only be called if manager types m@override and 
#enters correct password in employee code login section
def manager():
 print()
 print(" "*39,"\U0001F574"," Manager Access Portal",emoji.emojize(":bank:"))
 print()
 pd=input("Enter Master Code:")
 if pd=="man@suncb23":
 pass
 else:
 raise Exception("INCORRECT CODE>>SECURITY BREACH>>SHUTTING DOWN")
 print()
 print("WELCOME SANDEEP VERMA")
 print("1.View Employee List")
 print("2.View Bank Credentials")
 print("3.Exit")
 print("4.Continue")
 print("ANY OTHER INPUT WILL LEAD TO SECURITY BREACH LOCKDOWN OF MANAGER PORTAL")

 cho=int(input("Enter Choice (1-4):"))
 print()
 #To view employee list
 if cho==1:
 curs.execute("SELECT * FROM emplist")
 eml=curs.fetchall()
Page | 19
 print("(code, Name, Password)")
 for i in eml:
 print(i)
 #To access crucial secret data of bank
 elif cho==2:
 enf=open("bankSecureEncryptedDATA.dat",'rb')
 z=pickle.load(enf) #Deserialization/Unpickling
 enf.close()
 for i in z:
 print (i)
 elif cho==3:
 exit()
 elif cho==4:
 pass
 
 else:
 print("INVALID INPUT")
 raise Exception("SHUTTING DOWN>>>BREACH DETECTED")
#Employee Server Login/Registeration 
def login():
 flag=3
 print("Are you an existing employee?:(Y/N)",end=' ')
 empresp=input()
 empresp=empresp.upper()
 global loginb #Flag variable for login 
 global emppas
 loginb=False
Page | 20
 print()
 if empresp=='Y':
 while flag > 0: #Recursive Loop to limit permissible input upto 3 attempts
 print("Kindly Type in your 5 digit employee code:",end=' ')
 z=input()
 k=False
 if z==0:
 k=True
 global empcd
 empcd=z
 global emppas
 if z=='m@override':
 manager()
 print("Do you want to continue to Account Actions?(Enter Y to continue)")
 respn=input()
 if respn.upper()=='Y':
 empcd=0
 pass
 else:
 exit()
 else:
 pass
 #To check if input is an integer or not. Else flag-=1 i.e reduce available attempts
 if k==False:
 try:
Page | 21
 empcd=int(empcd)
 except:
 print("Kindly Type Only 5 digit Positive Integer")
 flag-=1
 print()
 continue
 else:
 empcd=0
 ##end of try block
 #To check if input is 5 digit integer or manager code or not
 if (len(str(empcd))==5) or empcd==0: 
 pas=int(input("Enter Password:"))
 
 print(empver.empverfun(empcd,pas))
 if empver.empverfun(empcd,pas)==("Employee Verified!"):
 loginb=True
 emppas=pas
 
 break
 else:
 pass
 else:
 print("Kindly type only 5 digit positive Code!")
 flag-=1
 print()
 if loginb==False and len(str(empcd))==5:
 print("Employee Not Found!!")
 print("Exiting")
 for i in range(10):
Page | 22
 print('.',end='')
 time.sleep(0.15)
 quit()
 elif empresp=="N":
 empreg.empregfun()
 print()
 print("Kindly Restart!")
 regb=True
 quit() 
 else:
 print("Invalid Input!! Can enter only Y or N")
 quit()
 
 if flag==0:
 print("Maximum Permissible Limit Reached. Exiting....")
 ##Time Delay Block
 for i in range(10):
 print('.',end='')
 time.sleep(0.15)
 quit()
login() #Func1 - To call object which runs login and registratiuon of employee
#Main Method to accomodate main menu functions
def main():
 print()
 print(" "*39,emoji.emojize(":derelict_house:"),"Main Menu")
Page | 23
 
 curs.execute("select Name from emplist where code="+str(empcd))
 empnm=curs.fetchone()
 print("Welcome ",empnm[0],"!!")
 for i in range(20):
 print('.',end='')
 time.sleep(0.05)
 curs.execute("select * from emplist where code="+str(empcd))
 empdt=curs.fetchall()
 global empname
 empname=empdt[0][1]
 #Printing Menu Options
 print()
 print("Select an Action:")
 print("1. Dashboard And Logged Activity")
 print("2. Create an Account")
 print("3. Deposit")
 print("4. Withdrawals")
 print("5. Transfer")
 print("6. Bank Statement")
 print("7. Loan Services")
 print("8. Close or Block an Account")
 print("9. Customer Complaints")
 print("10. Exit")
 print()
Page | 24
 global ch
 flag=4
 while flag>0: #Attempt Limiter Recursive Loop (ALRL)
 ch=input("Enter Choice (1-10):")
 try:
 ch=int(ch)
 except:
 print("Can enter only an Integer!")
 flag-=1
 continue
 if ch>0 and ch<11:
 break
 else:
 print("Enter only between 1 to 10")
 flag-=1
 if flag==0:
 print("Maximum Permissible Limit Reached!. Logging Out!")
 exit()
#### Login/Menu ends
if loginb==True:
 main()
#Bank Action Functions Definition Begin
#Dashboard function to show employee details and activity log
def dash():
 print()
 print(" "*39,emoji.emojize(":memo:"),"Dashboard")
 print()
 curs.execute("select * from emplist where code="+str(empcd))
Page | 25
 empdt=curs.fetchall()
 print("Employee Name:",empdt[0][1])
 print("Employee Code:",empdt[0][0])
 print()
 print()
 empdtt=str(empdt[0][0])
 print("Activity Log")
 empactfun.empactfunr(empdtt)
 
#Function which creates customer account
def cracct():
 print()
 print(" "*39,emoji.emojize(":man_frowning:")[0],"Create An Account") #emoji 
module gives this '🙍\u200d♂' output so we access only elem at 0th index 
 print()
 
 flag=3
 while flag>0: #ALRL
 print("Enter Employee Password to Proceed:",end="")
 empd=int(input())
 if len(str(empd))!=5:
 print("Invalid Password!!")
 flag-=1
 continue
 else:
 break
 if flag==0:

 print("Maximum Permssible Limit Reached!!. Quitting")
 quit()
 
 if empd==emppas:
 print("Access Granted!")
 print()

"""
 The following block will associate an account with a account number if and only
 if the employee adds the right passcode.
 Further it will allot a unique account number in a serial order i.e.i= 1000000001, 
 1000000002, 1000000003 and so on.
 The while loop checks if the i is already been alloted in the sql table 
 customeracct. When the loop intercepts a return type None,
 it will allot that integer to the present situation which provided the None return. 
 We Will call the following while block as
 auto number allocation system (ANAS)
 
"""
 
 i=1000000001
 acctnum=0
 while (i>1000000000): #ANAS
 exst="select * from customeracct where AcctNo="+str(i)
 curs.execute(exst)
 tempcd=curs.fetchone()
 if tempcd==None:
 acctnum=i
 
 print("Enter Customer Name:",end="")
 nm=input()

 nm="\'"+nm+"\'"
 bankbal=0
 actstat=1
 acctcr=datetime.date.today()
 acctcr=str(acctcr)
 acctcr='\''+acctcr+'\''
 dob=input("Enter date of birth (YYYY-MM-DD):")
 dob="\'"+dob+"\'"
 
 mob=(input("Enter 9-digit Mobile Number:"))
 
 email=input("Enter Email ID:")
 email="\'"+email+"\'"
 add=input("Enter Permanent Address:")
 add="\'"+add+"\'"
 
 ##Sql Value Insertion in customer account table
 est="insert into customeracct values 
("+str(acctnum)+','+nm+','+str(bankbal)+','+str(actstat)+','+acctcr+','+dob+','+str(mob)
+","+email+','+add+")"
 
 curs.execute(est)
 db.commit()
 print()
 print("Customer Account Created Successfully!")
 global emcds
 emcds=str(empcd)
 dt=datetime.datetime.now()
 dt=str(dt)
 dt='\''+dt+'\''
Page | 28
 #Sql employee action log insertion 
 curs.execute("select Name from emplist where code="+str(empcd))
 empname=curs.fetchone()
 
 empname = '\''+empname[0]+'\''
 empactfun.empactfunw(emcds,empname,dt,"\'Account Creation "+str(rand)+"\'")
 print()
 print("Server Request Code:",rand)
 
 break
 else:
 i+=1
 pass
 elif empd!=emppas:
 print("Incorrect Password. Exiting....")
 exit()
#Function to deposit money in account 
def dep():
 print()
 print(" "*39,emoji.emojize(":money_bag:"),"Money Deposit")
 print()
 print("Enter Account Number:",end='')
 acn=int(input())
 curs.execute("SELECT EXISTS(SELECT * from customeracct where AcctNo="+str(acn)+")")

 actex=curs.fetchone()
 #Abv Stmnts - tuple having 1 i.e. [(1,)] if account exists else tuple having 0 i.e., [(0,)]
 if actex[0]==0: #Account Existence Confirmer AEC
 print("Account Does Not Exist!!")
 print("Exiting.....")
 quit()
 else:
 curs.execute("select * from customeracct where AcctNo="+str(acn))
 cdet=curs.fetchone()
 detdict=dict() #Dictionary to store customer account details
 detdict['Account_No']=cdet[0]
 detdict['Customer_Name']=cdet[1]
 detdict['Balance']=cdet[2]
 detdict['Status']=cdet[3] #Will store 1 if actt is active else 0
 if detdict['Status']==1:
 detdict['Status']='Active'
 else:
 detdict['Status']='Blocked'
 detdict['Account_Created']=cdet[4]
 detdict['Date Of Birth']=cdet[5]
 detdict['Mobile_No']=cdet[6]
 detdict['Email']=cdet[7]
 if detdict['Status']=='Blocked':
 print("The account is blocked. Kindly unblock to proceed.")
 time.sleep(2)
Page | 30
 raise Exception("Account Is BLOCKED. Permission to access=False")
 
 else:
 pass
 headings=detdict
 headings=tuple(headings)
 
 data=detdict.values()
 data=tuple(data)
 
 for i in headings:
 print(i,end="\t")
 print()
 for j in data:
 print(j,end="\t ")
 print("\n\n")
 print("Enter Amount To be Deposited:",end='')
 amdep=int(input())
 print()
 empvp=int(input("Enter Passcode to Proceed:"))
 newbal=detdict['Balance']+amdep
 if empver.empverfun(empcd,empvp)==("Employee Verified!"):
 curs.execute("UPDATE customeracct SET BankBal="+str(newbal)+" where AcctNo="+str(acn))
 db.commit()
 detdict['Balance']+=amdep
Page | 31
 #LoadScreenBar
 loadf.loadbar(ch) 
 print("\n\n")
 print("Amount Deposited Successfully!!")
 print()
 headings=detdict
 headings=tuple(headings)
 
 data=detdict.values()
 data=tuple(data)
 z1=''
 z2=''
 
for i in headings:
 print(i,end="\t")
 
 print()
 for j in data:
 print(j,end="\t ")
 
 #Sql employee action log insertion
 dt=datetime.datetime.now()
 dt=str(dt)
 dt='\''+dt+'\''
 curs.execute("select Name from emplist where code="+str(empcd))
 empname=curs.fetchone()
 enm=empname[0].upper() 
 empname = '\''+empname[0]+'\''
 empactfun.empactfunw(str(empcd),empname,dt,"\'Money Deposited "+str(rand)+"\'")
 print()

 #Organising data to create pdf
 AN=detdict['Account_No']
 CN = detdict['Customer_Name']
 IB = detdict['Balance']+amdep
 FB = detdict['Balance']
 M = amdep
 EN = enm
 RN = "Deposit"
 task ="Money Deposit"
 ACT="Money Deposited"
 autopdf.pdfn(task, AN, CN,IB, FB, M,EN,RN,ACT)
 
 #Saving in Bank Statement
 dt=datetime.date.today()
 dt=str(dt)
 dt='\''+dt+'\''
 acn=str(acn)
 acn='\''+acn+'\''
 curs.execute("INSERT INTO custstmnt values("+acn+','+dt+","+"\'Money Deposited To Self- "+str(amdep)+"\')")
 db.commit()
 print("Server Request Code:",rand)
 
 else:
 print("Invalid Password/Employee Does Not Exist!")
 quit()
 #Function to withdraw money from account 
def withd():
 print()

 print(" "*39,emoji.emojize(":dollar_banknote:"),"Money Withdrawal")
 print()
 print("Enter Account Number:",end='')
 acn=int(input())
 curs.execute("SELECT EXISTS(SELECT * from customeracct where AcctNo="+str(acn)+")")
 actex=curs.fetchone()
 #Abv Stmnts - tuple having 1 i.e. [(1,)] if account exists else tuple having 0 i.e., [(0,)]

if actex[0]==0: #AEC
 print("Account Does Not Exist!!")
 print("Exiting.....")
 quit()
 
else:
 curs.execute("select * from customeracct where AcctNo="+str(acn))
 cdet=curs.fetchone()
 detdict=dict() #Dictionary to store customer account details
 detdict['Account_No']=cdet[0]
 detdict['Customer_Name']=cdet[1]
 detdict['Balance']=cdet[2]
 detdict['Status']=cdet[3] #Will store 1 if actt is active else 0
 #Following checks if account is blocked or not 
 
if detdict['Status']==1:
 detdict['Status']='Active'

else:
 detdict['Status']='Blocked'
 detdict['Account_Created']=cdet[4]
 detdict['Date Of Birth']=cdet[5]

 detdict['Mobile_No']=cdet[6]
 detdict['Email']=cdet[7]
 
if detdict['Status']=='Blocked':
 print("The account is blocked. Kindly unblock to proceed.")
 time.sleep(2)
 raise Exception("Account Is BLOCKED. Permission to access=False")
 else:
 pass
 headings=detdict
 headings=tuple(headings)
 
 data=detdict.values()
 data=tuple(data)
 

for i in headings:
 print(i,end="\t")
 print()
 
for j in data:
 print(j,end="\t ")
 print("\n\n")
 
 print("Enter Amount To be Withdrawed:",end='')
 amdep=int(input())
 print()
 empvp=int(input("Enter Passcode to Proceed:"))
 newbal=detdict['Balance']-amdep


if newbal<0:
 print("Insufficient Funds. Withdraw Unsuccesful!!")
 raise Exception("FUNDS INSUFFICIENT")

 

if empver.empverfun(empcd,empvp)==("Employee Verified!"):
 curs.execute("UPDATE customeracct SET BankBal="+str(newbal)+" where AcctNo="+str(acn))
 db.commit()
 detdict['Balance']-=amdep
 print("Processing")
 #LoadScreenBar
 loadf.loadbar(ch)
 print("Kindly collect the money from the vendor!") 
 print("\n\n")
 headings=detdict
 headings=tuple(headings)
 data=detdict.values()
 data=tuple(data)
 

for i in headings:
 print(i,end="\t")
 print()
 
for j in data:
 
 print(j,end="\t ")
 #Sql employee action log insertion
 dt=datetime.datetime.now()
 dt=str(dt)
 dt='\''+dt+'\''
 curs.execute("select Name from emplist where code="+str(empcd))
 empname=curs.fetchone()
Page | 36
 enm=empname[0].upper()
 empname = '\' '+empname[0]+'\' ' #To get ‘something’ for sql command
 empactfun.empactfunw(str(empcd),empname,dt,"\'Money Withdrawed \"+str(rand)+"\'")
 
 print()
 
#Organising data to create pdf

 AN=detdict['Account_No']
 CN = detdict['Customer_Name']
 IB = detdict['Balance']+amdep
 FB = detdict['Balance']
 M = amdep
 EN = enm
 RN = "Withdraw"
 task ="Money Withdrawal"
 ACT="Money Withdrawn"
 autopdf.pdfn(task, AN, CN,IB, FB, M,EN,RN,ACT)
 
#Saving in Bank Statement
 dt=datetime.date.today()
 dt=str(dt)
 dt='\''+dt+'\''
 acn=str(acn)
 acn='\''+acn+'\''
 curs.execute("INSERT INTO custstmnt values("+acn+','+dt+","+"\'Money Withdrawal To Self -"+str(amdep)+"\')")
 db.commit()
 print("Server Request Code:",rand)
 
 
else:

 print("Invalid Password/Employee Does Not Exist!")
 quit()
#Function to trasnfer money from one account to another 

def trans():
 print()
 print(" "*39,emoji.emojize(":money_with_wings:"),"Money Transfer")
 print()
 print("Enter FROM Account Number:",end='')
 acn=int(input())
 print("Enter TO Account Number:",end="")
 acnt=int(input())
 
 curs.execute("SELECT EXISTS(SELECT * from customeracct where AcctNo="+str(acn)+")")
 actex=curs.fetchone()
 curs.execute("SELECT EXISTS(SELECT * from customeracct where AcctNo="+str(acnt)+")")
 acttex=curs.fetchone()
 #Abv Stmnts - tuple having 1 i.e. [(1,)] if account exists else tuple having 0 i.e., [(0,)]

  if actex[0]==0 or acttex[0]==0:

  print("Account Does Not Exist!!")
  print("Exiting.....")
  quit()

else:
 curs.execute("select * from customeracct where AcctNo="+str(acn))
 cdet=curs.fetchone()
 detdict=dict() #Dictionary to store customer account details

 detdict['Account_No']=cdet[0]
 detdict['Customer_Name']=cdet[1]
 detdict['Balance']=cdet[2]
 detdict['Status']=cdet[3] #Will store 1 if actt is active else 0

if detdict['Status']==1:
 detdict['Status']='Active'
 
else:
 detdict['Status']='Blocked'
 detdict['Account_Created']=cdet[4]
 detdict['Date Of Birth']=cdet[5]
 detdict['Mobile_No']=cdet[6]
 detdict['Email']=cdet[7]
 curs.execute("select * from customeracct where AcctNo="+str(acnt))
 cdett=curs.fetchone()
 
if detdict['Status']=='Blocked' or cdett[3]==0:
 print("The account is blocked. Kindly unblock to proceed.")
 time.sleep(2)
 raise Exception("Account Is BLOCKED. Permission to access=False")
 

else:
 pass
 headings=detdict
 headings=tuple(headings)
 
 data=detdict.values()
 data=tuple(data)
 

 for i in headings:
 print(i,end="\t")
 print()
 for j in data:
 print(j,end="\t ")
 print("\n\n")
 
 print("Enter Amount To be Transferred:",end='')
 amdep=int(input())
 print()
 empvp=int(input("Enter Passcode to Proceed:"))
 curs.execute("select * from customeracct where AcctNo="+str(acn))
 balt=curs.fetchone()
 balt = balt[2]
 curs.execute("select * from customeracct where AcctNo="+str(acnt))
 newbalt=curs.fetchone()
 newbalt=newbalt[2]
 newbalt=newbalt+amdep
 
 newbal=detdict['Balance']-amdep
 
 if newbal<0: #If money transfer amount more than avl balance than it wont occur
 print("Insufficient Funds. Withdraw Unsuccesful!!")
 raise Exception("FUNDS INSUFFICIENT")
 
 if empver.empverfun(empcd,empvp)==("Employee Verified!"):
 curs.execute("UPDATE customeracct SET BankBal="+str(newbal)+" where AcctNo="+str(acn))
 db.commit()

 detdict['Balance']-=amdep
 
 curs.execute("UPDATE customeracct SET BankBal="+str(newbalt)+" where AcctNo="+str(acnt))
 db.commit()
 print("Processing")
 #LoadScreenBar
 loadf.loadbar(ch)
 print("Money Transfer is Successful!") 
 print("\n\n")
 headings=detdict
 headings=tuple(headings)
 data=detdict.values()
 data=tuple(data)
 
 for i in headings:
 print(i,end="\t")
 print()
 for j in data:
 print(j,end="\t ")
 #Sql employee action log insertion
 dt=datetime.datetime.now()
 dt=str(dt)
 dt='\''+dt+'\''
 curs.execute("select Name from emplist where code="+str(empcd))
 empname=curs.fetchone()
 enm=empname[0].upper()
Page | 41
 empname = '\' '+empname[0]+'\' '
 empactfun.empactfunw(str(empcd),empname,dt,"\'Money Transferred "+str(rand)+"\'")
 print()
 #Organising data to create pdf
 AN=detdict['Account_No']
 CN = detdict['Customer_Name']
 IB = detdict['Balance']+amdep
 FB = detdict['Balance']
 M = amdep
 EN = enm
 RN = "Transfer"
 task ="Money Transfer"
 ACT="Money Transferred"
 autopdf.pdfn(task, AN, CN,IB, FB, M,EN,RN,ACT)
 #Saving in Bank Statement
 dt=datetime.date.today()
 dt=str(dt)
 dt='\''+dt+'\''
 acn=str(acn)
 acn='\''+acn+'\''
 curs.execute("INSERT INTO custstmnt values("+acn+','+dt+","+"\'Money Transfer To "+str(acnt)+"\')")
 db.commit()
 print("Server Request Code:",rand)
 
 else:
 print("Invalid Password/Employee Does Not Exist!")

 quit()
#Function to access the bank statment table in sql that stores customer account 
activities
def bnst():
 print()
 print(" "*39,emoji.emojize(":dollar_banknote:"),"Bank Statement")
 print()
 print("Enter Account Number:",end='')
 acn=int(input())
 curs.execute("SELECT EXISTS(SELECT * from customeracct where AcctNo="+str(acn)+")")
 actex=curs.fetchone()
 #Abv Stmnts - tuple having 1 i.e. [(1,)] if account exists else tuple having 0 i.e., [(0,)]
 if actex[0]==0:
 print("Account Does Not Exist!!")
 print("Exiting.....")
 quit()
 else:
 curs.execute("select * from customeracct where AcctNo="+str(acn))
 cdet=curs.fetchone()
 detdict=dict() #Dictionary to store customer account details
 detdict['Account_No']=cdet[0]
 detdict['Customer_Name']=cdet[1]
 detdict['Balance']=cdet[2]
 detdict['Status']=cdet[3] #Will store 1 if actt is active else 0
Page | 43
 if detdict['Status']==1:
 detdict['Status']='Active'
 else:
 detdict['Status']='Blocked'
 detdict['Account_Created']=cdet[4]
 detdict['Date Of Birth']=cdet[5]
 detdict['Mobile_No']=cdet[6]
 detdict['Email']=cdet[7]
 if detdict['Status']=='Blocked':
 print("The account is blocked. Kindly unblock to proceed.")
 time.sleep(2)
 raise Exception("Account Is BLOCKED. Permission to access=False")
 
 else:
 pass
 headings=detdict
 headings=tuple(headings)
 
 data=detdict.values()
 data=tuple(data)
 
 for i in headings:
 print(i,end="\t")
 print()
 for j in data:
 print(j,end="\t ")
 print("\n\n")
 curs.execute("select * from custstmnt where AcctNo="+str(acn))
Page | 44
 det=curs.fetchall()
 print("Date \t\t\t Action")
 for i in det:
 print(i[1],"\t\t",i[2])
 #Creating a pdf receipt
 pdf=FPDF()
 pdf.add_page()
 pdf.set_font("Arial", size=21)
 pdf.cell(200,10,txt="Sunrise Chartered Bank",ln=1,align='C')
 dtn=datetime.datetime.now()
 dtn=str(dtn)
 pdf.set_font("Arial", size=16)
 pdf.cell(200,10,txt=dtn,ln=2,align='C')
 pdf.set_font("Arial", size=12)
 pdf.cell(200,10,txt="Bank Statement",ln=4,align='C')
 pdf.cell(200,10,txt="-"*50,ln=7,align='C')
 pdf.cell(200,10,txt=" Account Number: "+str(acn),ln=8,align='L')
 pdf.cell(200,10,txt="Customer Name: 
"+str(detdict['Customer_Name']),ln=9,align='L')
 pdf.cell(200,10,txt="Date \t\t\t\t Action",ln=12,align='L')
 for i in det:
 pdf.cell(200,10,txt=str(i[1])+"\t\t"+i[2],ln=13,align='L')
 pdf.cell(200,10,txt="Manager",ln=22,align='R')
 pdf.cell(200,10,txt="Sandeep Verma",ln=23,align='R')
 pdf.cell(200,10,txt="-"*50,ln=18,align='C')
Page | 45
 pdf.cell(200,10,txt="Bank will not be responsible for any losses or inadvertent 
errors",ln=20,align='C')
 
 
 out=str(detdict['Account_No'])+"_Account_Stmnt_"
 pdf.output(out+".pdf")
 print("Server Request Code:",rand)
 
#Function to create,view and repay loan
def loan():
 print()
 print(" "*39,emoji.emojize(":closed_book:"),"Loan Services")
 print()
 
 print("1. Create new Loan Account")
 print("2. View Loan Account")
 print("3. Repay Loan Debt")
 cho=int(input("Enter Your Choice(1-3)"))
 print("\n\n")
 
 if cho==1:
 i=1000000001
 acctnum=0
 while (i>1000000000):
 exst="select * from loanacct where LAcctNo="+str(i)
 curs.execute(exst)
 tempcd=curs.fetchone()
 if tempcd==None:
Page | 46
 acctnum=i
 
 print("Enter Customer Name:",end="")
 nm=input()
 nm="\'"+nm+"\'"
 bankbal=0
 actstat=1
 acctcr=datetime.date.today()
 acctcr=str(acctcr)
 acctcr='\''+acctcr+'\''
 lamt=int(input("Enter Loan Amount:"))
 rsn=input("Enter Reason for Loan:")
 rsn="\'"+rsn+"\'"
 dd=input("Enter Due date (YYYY-MM-DD):")
 dd="\'"+dd+"\'"
 
 mob=(input("Enter 9-digit Mobile Number:"))
 
 email=input("Enter Email ID:")
 email="\'"+email+"\'"
 dt=acctcr
 ##Sql Value Insertion
 est="INSERT INTO loanacct values 
("+str(acctnum)+','+nm+','+str(lamt)+','+rsn+','+dd+','+mob+','+email+","+dt+")"
 
 curs.execute(est)
 db.commit()
Page | 47
 print()
 print("Loan Account Created Successfully!")
 bacn=int(input("Enter Bank Account Number:"))
 curs.execute("select * from customeracct where AcctNo="+str(bacn))
 cdet=curs.fetchone()
 newbal=cdet[2]+lamt
 curs.execute("UPDATE customeracct SET BankBal="+str(newbal)+" where AcctNo="+str(bacn))
 db.commit()
 emcds=str(empcd)
 dt=datetime.datetime.now()
 dt=str(dt)
 dt='\''+dt+'\''
 #Sql employee action log insertion
 curs.execute("select Name from emplist where code="+str(empcd))
 empname=curs.fetchone()
 
 empname = '\''+empname[0]+'\''
 
 empactfun.empactfunw(emcds,empname,dt,"\'Loan Account Created "+str(rand)+"\'")
 print()
 print("Loan Money Deposited")
 print("Server Request Code:",rand)
 break
 else:
Page | 48
 i+=1
 
elif cho==2:
 lacn=int(input("Enter Loan Account Number:"))
 curs.execute("select * from loanacct where Lacctno="+str(lacn))
 det=curs.fetchone()
 print("Name:",det[1])
 print("Loan Amount:",det[2])
 print("Due Date:",det[4])
 
 elif cho==3:
 lacn=int(input("Enter Loan Account Number:"))
 curs.execute("SELECT EXISTS(SELECT * from loanacct where LacctNo="+str(lacn)+")")
 actex=curs.fetchone()
 #Abv Stmnts - tuple having 1 i.e. [(1,)] if account exists else tuple having 0 i.e., 
[(0,)]
 if actex[0]==0:
 print("Loan Account Does Not Exist!!")
 print("Exiting.....")
 quit()
 else:
 pass
 conf=input("Confirm?(Y/N)")
 if conf.upper()=='N' or conf.upper()!='Y':
 print("Cancelled")
 quit()
 elif conf.upper()=='Y':
Page | 49
 pass
 emcds=str(empcd)
 
 curs.execute("select * from loanacct where Lacctno="+str(lacn))
 det=curs.fetchone()
 amt=det[2]
 
 curs.execute("UPDATE loanacct SET loanamt=0 where LacctNo="+str(lacn))
 db.commit()
 print("Processing")
 #LoadScreenBar
 loadf.loadbar(ch)
 print("\nKindly Take Cheque Payment from the Customer!. Server Process Completed")
 print("Detailed Acknowledgement will be mailed to the customer within 3 business days")
 
 print("Enter Cheque Number:",end=''); chq=int(input())
 print("Server Request Code:",rand)
 print("Server Process Completed")
 
 #Creating a pdf receipt
 pdf=FPDF()
 pdf.add_page()
 pdf.set_font("Arial", size=21)
 pdf.cell(200,10,txt="Sunrise Chartered Bank",ln=1,align='C')
Page | 50
 dtn=datetime.datetime.now()
 dtn=str(dtn)
 pdf.set_font("Arial", size=16)
 pdf.cell(200,10,txt=dtn,ln=2,align='C')
 pdf.set_font("Arial", size=12)
 pdf.cell(200,10,txt=det[3]+" Loan Repayment Receipt",ln=4,align='C')
 pdf.cell(200,10,txt="-"*50,ln=7,align='C')
 pdf.cell(200,10,txt="Loan Account Number: "+str(lacn),ln=8,align='L')
 pdf.cell(200,10,txt="Customer Name: "+(det[1]),ln=9,align='L')
 pdf.cell(200,10,txt="Date: "+dtn,ln=10,align='L')
 pdf.cell(200,10,txt="Payment Done: "+(str(amt)),ln=12,align='L')
 pdf.cell(200,10,txt="Cheque Number: "+(str(chq)),ln=13,align='L')
 pdf.cell(200,10,txt="Manager",ln=22,align='R')
 pdf.cell(200,10,txt="Sandeep Verma",ln=23,align='R')
 pdf.cell(200,10,txt="-"*50,ln=18,align='C')
 pdf.cell(200,10,txt="Bank will not be responsible for any losses or inadvertent errors.",ln=20,align='C')
 pdf.cell(200,10,txt="Repayment Acknowledgement subject to cheque realisation*",ln=21,align='C')
 out=str(lacn)+"_Loan_Repay_Receipt"
 pdf.output(out+".pdf")
 #Sql employee action log insertion
 dt=datetime.datetime.now()
 dt=str(dt)
 dt='\''+dt+'\''
 emcds=str(empcd)
 curs.execute("select Name from emplist where code="+str(empcd))

 empname=curs.fetchone()
 
 empname = '\' '+empname[0]+'\' '
 
 empactfun.empactfunw(emcds,empname,dt,"\'Loan Repayment Initiated "+str(rand)+"\'")
 print()
 print("Server Request Code:",rand)
 
 
#Function to block or unblock an account
def actmng():
 print()
 print(" "*39,emoji.emojize(":money_bag:"),"Account Block Management")
 print()
 print("Enter Account Number:",end='')
 acn=int(input())
 curs.execute("SELECT EXISTS(SELECT * from customeracct where AcctNo="+str(acn)+")")
 actex=curs.fetchone()
 #Abv Stmnts - tuple having 1 i.e. [(1,)] if account exists else tuple having 0 i.e., [(0,)]
 if actex[0]==0:
 print("Account Does Not Exist!!")
 print("Exiting.....")
 raise Exception("ACCOUNT DOES NOT EXIST")
 else:
 pass

 curs.execute("select * from customeracct where AcctNo="+str(acn))
 cdet=curs.fetchone()
 detdict=dict() #Dictionary to store customer account details
 detdict['Account_No']=cdet[0]
 detdict['Customer_Name']=cdet[1]
 detdict['Balance']=cdet[2]
 detdict['Status']=cdet[3] #Will store 1 if actt is active else 0
 if detdict['Status']==1:
 detdict['Status']='Active'
 else:
 detdict['Status']='Blocked'
 detdict['Account_Created']=cdet[4]
 detdict['Date Of Birth']=cdet[5]
 detdict['Mobile_No']=cdet[6]
 detdict['Email']=cdet[7]
 headings=detdict
 headings=tuple(headings)
 
 data=detdict.values()
 data=tuple(data)
 
 for i in headings:
 print(i,end="\t")
 print()
 for j in data:
 print(j,end="\t ")
Page | 53
 print("\n\n")
 dt=datetime.date.today()
 dt=str(dt)
 dt='\''+dt+'\''
 st=input("TYPE B TO BLOCK AND U TO UNBLOCK THE ACCOUNT:")
 #To block
 if st.upper()=='B':
 curs.execute("UPDATE customeracct SET actstatus=0 where acctNo="+str(acn))
 db.commit()
 print("Account Blocked")
 #Sql employee action log insertion
 curs.execute("select Name from emplist where code="+str(empcd))
 empname=curs.fetchone()
 
 empname = '\''+empname[0]+'\''
 emcds=str(empcd)
 empactfun.empactfunw(emcds,empname,dt,"\'Account Blocked "+str(rand)+"\'")
 print()
 print("Server Request Code:",rand)
 
 #To unblock 
 elif st.upper()=='U':
 curs.execute("UPDATE customeracct SET actstatus=1 where acctNo="+str(acn))
 db.commit()
Page | 54
 print("Account UnBlocked")
 #Sql employee action log insertion
 curs.execute("select Name from emplist where code="+str(empcd))
 empname=curs.fetchone()
 
 empname = '\' '+empname[0]+'\' '
 emcds=str(empcd) 
 empactfun.empactfunw(emcds,empname,dt,"\'Account UnBlocked "+str(rand)+"\'")
 print()
 print("Server Request Code:",rand)
 
 
 else:
 print("INCORRECT INPUT.")
 raise Exception("Invalid Input encountered in security portal.Exit")
 
#Function to create a complaint receipt 
def compl():
 print(" "*39,emoji.emojize(":busts_in_silhouette:"),"Complaints")
 acn=int(input("Enter Account Number:"))
 curs.execute("SELECT EXISTS(SELECT * from customeracct where AcctNo="+str(acn)+")")
 actex=curs.fetchone()
 #Abv Stmnts - tuple having 1 i.e. [(1,)] if account exists else tuple having 0 i.e., [(0,)]
 if actex[0]==0:
 print("Account Does Not Exist!!")
Page | 55
 raise Exception("ACCOUNT NOT FOUND$$ COMPLAINT FAILED")
 
 else:
 pass
 
 nm=input("Enter Customer Name:")
 print()
 comp=input("Enter Customer Complaint:")
 tkn=int(input("Kindly assign a token number:"))
 
 #Creating a pdf Complaint
 pdf=FPDF()
 pdf.add_page()
 pdf.set_font("Arial", size=21)
 pdf.cell(200,10,txt="Sunrise Chartered Bank",ln=1,align='C')
 dtn=datetime.datetime.now()
 dtn=str(dtn)
 pdf.set_font("Arial", size=16)
 pdf.cell(200,10,txt=dtn,ln=2,align='C')
 pdf.set_font("Arial", size=12)
 pdf.cell(200,10,txt="Customer Complaint",ln=4,align='C')
 pdf.cell(200,10,txt="-"*50,ln=7,align='C')
 pdf.cell(200,10,txt="Account Number: "+str(acn),ln=8,align='L')
 pdf.cell(200,10,txt="Customer Name: "+(nm),ln=9,align='L')
 pdf.cell(200,10,txt="Date: "+dtn,ln=10,align='L')
 pdf.cell(200,10,txt="Token Number: "+(str(tkn)),ln=13,align='L')
Page | 56
 pdf.cell(200,10,txt="Complaint: "+(comp),ln=13,align='L')
 pdf.cell(200,10,txt="Grievance Cell Coordinator",ln=25,align='R')
 pdf.cell(200,10,txt="_________________",ln=26,align='R')
 pdf.cell(200,10,txt="Pooja Mehra",ln=27,align='R')
 pdf.cell(200,10,txt="-"*50,ln=29,align='C')
 pdf.cell(200,10,txt="Bank will not be responsible for any losses or inadvertent errors.",ln=30,align='C')
 pdf.cell(200,10,txt="Complaint processing may take 4-5 Business Days*",ln=31,align='C')
 
 
 out=str(acn)+"_Complaint__Receipt"
 pdf.output(out+".pdf")
 #Sql employee action log insertion
 dt=datetime.date.today()
 dt=str(dt)
 dt='\''+dt+'\''
 curs.execute("select Name from emplist where code="+str(empcd))
 empname=curs.fetchone()
 
 empname = '\''+empname[0]+'\''
 emcds=str(empcd)
 empactfun.empactfunw(emcds,empname,dt,"\'Loan Repayment Initiated "+str(rand)+"\'")
 print()
 print("Server Request Code:",rand)
 
Page | 57
#Calling functions based on user(employee) choice
if ch==1:
 dash()
elif ch==2:
 cracct()
elif ch==3:
 dep()
elif ch==4:
 withd()
elif ch==5:
 trans()
elif ch==6:
 bnst()
elif ch==7:
 loan()
elif ch==8:
 actmng()
elif ch==9:
 compl()
elif ch==10:
 print("Exiting")
 for i in range(20):
 print('.',end='')
 time.sleep(0.10)
 quit()
 
#Note wherever you see ‘\’’ it means ‘\’ ‘ i.e to get a ‘ in output
#For traversing majorly tuples are used as they are immutable and faster
#curs.fetchall gives a list of tuples while curs.fethchone gives a tuple only

#All files must be saved in same folder as python to get desired output

  #NOTE: Kindly ignore and remove PAGE|xx from lines there would be many.

#Indentations weren't preserved in transferring the code. Kindly indent as required or follow my LinkedIN page Sonit Patil to view its pdf version
