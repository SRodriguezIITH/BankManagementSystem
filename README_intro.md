# BankManagementSystem
It contains the source code for python front-end and a MySQL backend

This project is based upon management software of banking activities like 
account creation, deposits, transfer, etc. created through the Python 
Software. This bank software is meant for bank employees/manager.
The program will have an interface with SQL database. Database store 
tables of customer account, loan account, employee list, action log and 
bank statement which will be accessed throughout the program in various 
functions(). 
On running the program, there will be a employee login/registration block. It 
will ask for employee code and password and on successful verification 
through SQL stored data, it will continue. Manager can override here and 
open a secret manager portal accessible through master code. Further it 
must display available banking options. Each banking option will have 
separate functions/methods created. Each function accesses respective 
data from SQL and stores something in it. Also an employee activity log is 
maintained for every function he/she executes.
functions() in order of menu are:

1. manager() =Secret encrypted portal for manager (Not in Menu)
2. login() = To facilitate a login/registration page(Verification)
3. main() =Display available menu options
4. dash()=Displays logged in employee details and activity log
5. cracct() = Facilitates creation and allocation of account number
6. dep()=Facilitate depositing money in respective account number
7. withd()=Facilitates withdrawal of money from respective account
8. trans() = Facilitates money transfer from one account to another
9. bnst() = Accesses bank statement from sql and displays it for 
inputted account number
10. loan() = To create/view/repay loan account
11. actmng() = To block/Unblock a Number
12. compl() = To create a complaint receipt
13. 
Account created can be blocked/unblocked and only unblocked accounts 
can undergo banking options.Some Functions creates a pdf receipt using 
Page | 7
fpdf library. Top secret bank data is saved in a binary file so that it is 
human unreadable.

#Python/Other Concept Prerequisites—
1. All Basics + Strings, tuples, lists and dictionary
2. Modules – time, datetime, emoji, pickle, mysql.connector(), fpdf and 
random and Self Defined Module - BankSecurityPassage
3. Functions
4. UNICODE [for multilingual computing]
5. Conditional constructs – if..elif...else, if..else, nested if... else, etc.
6. Operators including membership operators.
7. Iterative Constructs and Recursion
8. Computational Thinking – Coding, Testing, Debugging.
9. MySQL & its interface with IDLE
10. Binary File Handling
11. 
We will be naming our Bank Management Software –
Sunrise Chartered Bank System Portal

Manager Name will be = Sandeep Verma
Manager Override Code = “m@override”( in employee code input line)
Manager Master Code will be = man@suncb23

NOTE: The indentations weren't preserved as I transferred my cod efrom IDE to git. As the number of lines of code were heavy for me to re-indent, they have been left as it is. Kindly indent as required
