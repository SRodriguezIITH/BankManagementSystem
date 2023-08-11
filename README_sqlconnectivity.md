While creating real-life software, it becomes immensely necessary that 
certain data is permanently stored (A real life software is a full-stack 
program). In our project, we may need to store customer account details, his 
bank balance, his bank statement, etc. All this can be achieved my interface 
with SQL Database.
SQL or Structured Query Language is a unified, non-procedural language 
used to create and manage databases. A database is an organized 
collection of data. All data can be stored properly in tables, records, etc. and 
can be updated and accessed anytime.
We will use MySQL for our SQL programming because it is a open source 
database management system which provides excellent features like 
creating and accessing data in a tabular format.
Components of our interface:
IDLE Python(Front-End) = used to take input and show output; basically what the user 
sees.
MySQL(Back-End) = used to store required data, manipulate it and access it may or 
may not based on python input.

1. Install MySQL connector from cmd by typing 
pip install my-sql-connector-python

2. import mysql.connector() in IDLE script

3. Establish connection by:
db=mysql.connector.connect(host=”localhost”,user=’root’,passwd=’<p
assword>‘, database=”<database_name>”)

4. Create Cursor Object by:
curs = db.cursor()

5. Execute by curs.execute(“<SQL command>”)

6. Use db.commit() for insert/update commands
Now for our project, we have pre done the following steps:

1. Created database scb_bank with host=”localhost”, user=”root”, passwd 
=”Sonit@123”

2. Created the following tables with following description(back-end
