print('-----BANK MANAGEMENT SYSTEM - ASPRV224 BANK-----')
print('-------MADE BY:PARTH THAKKAR-------')
from tabulate import tabulate
import time
k=time.localtime()
date=str(k[0])+'-'+str(k[1])+'-'+str(k[2])
tme=str(k[3])+':'+str(k[4])+':'+str(k[5])
print("Today's date:- ",date,"   Time:- ",tme)
import mysql.connector
connection = mysql.connector.connect(host='localhost',
                                              database='bm',
                                              user='root',
                                              password='root',
                                              charset = 'utf8')
cursor= connection.cursor()
while(True):
 print('-'*30)
 print("""
 Main Menu
 1. Add customer
 2. Remove customer
 3. Withdraw Amount
 4. Deposit Amount 
 5. Show customer Details
 6. Print Passbook
 7. Our Customers
 8. exit""")
 print('-'*30)
 ch=int(input("Enter Your Choice:"))
 while(ch<1 or ch>8):
     print("Enter Valid Choice")
     ch=int(input("Enter Your Choice:"))
 import random
 if(ch==1):
     pas=str(random.randint(1111111111,9999999999))
     pas=str(pas)
     n=input("Enter Your Full Name:")
     m=int(input("Enter Your Mobile Number:"))
     while(len(str(m))!=10):
         print("Enter Valid Input..")
         m=int(input("Enter Your Mobile Number:"))
     m=str(m)
     am=int(input("Enter initial Amount To Deposite(minimum 500 required):"))
     while(am<500):
         print('not enough amount...')
         am=int(input("Enter initial Amount To Deposite(minimum 500 required):"))
     print("Your Account Number Is  ***",pas,'***')
     sp1="insert into bm (name,mobile_number,amount,account_number) values(%s,%s,%s,%s);"
     tup=(n,m,am,pas)
     cursor.execute(sp1,tup)
     connection.commit()
 elif(ch==2):
     p1=input("Enter Your Bank Account Number:")
     p=(p1,)
     sq2="delete from bm where account_number = %s;"
     cursor.execute(sq2,p)
     connection.commit()
 elif(ch==3 or ch==5):
     l=[]
     ya=''
     p1=input("Enter Your Bank Account Number:")
     sq3="select * from bm;"
     cursor.execute(sq3)
     for i in cursor:
         if(i[3]==p1):
             ya=int(i[2])
             l=list(i)
     if(ya==''):
       print("Account Does Not Exist..")
     else:
       if(ch==5):
        print('Your Name:-',l[0])
        print('Your Mobile Number:-',l[1])
        print('Your Current Balance:-',l[2])
        print('Your Account Number:-',l[3])
       else:
        print("Your Current Balance is ",ya)
        wa=int(input("Enter Amount to Withdraw:"))
        while(ya-wa<500):
            print("You Have to Keep Minimum 500Rs")
            wa=int(input("Enter Amount to Withdraw:"))
        p=(ya-wa,p1,)
        sq4="update bm set amount = %s where account_number = %s;"
        cursor.execute(sq4,p)
        connection.commit()
        print('Processing Your Transaction...  please wait!')
        print('.')
        print('.')
        print('.')
        k=time.localtime()
        sec=str(k[5])
        sec=int(sec)
        nsec=sec+6
        if(nsec>60):
            nsec=nsec-60
        while True:
            k1=time.localtime()
            sec1=str(k1[5])
            sec1=int(sec1)
            if(nsec==sec1):
                print(' ')
                break

        
        print("*** Ammount Withdrawal Successfully.. ***")
        sq7='insert into passbook (account_number, type, amount,date) values(%s,%s,%s,%s);' 
        pt=(p1,'Credit',wa,date,)
        cursor.execute(sq7,pt)
        connection.commit()
 elif(ch==4):
     ya=''
     p1=input("Enter Your Bank Account Number:")
     sq5="select * from bm;"
     cursor.execute(sq5)
     for i in cursor:
         if(i[3]==p1):
             ya=int(i[2])
     if(ya==''):
       print("Account Does Not Exist..")
     else:
         try:
           da=int(input("Enter Amount To deposit:"))
           tup=(ya+da,p1,)
           sq6="update bm set amount = %s where account_number = %s;"
           cursor.execute(sq6,tup)
           connection.commit()
           print("Cash Added successfully..")
         except:
             print("Failed to Add Cash.. Retry!")
     sq8='insert into passbook (account_number, type, amount,date) values(%s,%s,%s,%s);' 
     pt=(p1,'Debit',da,date,)
     cursor.execute(sq8,pt)
     connection.commit()
 elif(ch==6):
     main=[]
     pas=input("Enter Your Bank Account Number:")
     sq9='select * from passbook;'
     cursor.execute(sq9)
     for i in cursor:
         if(i[0]==pas):
             l=list(i)
             main.append(l)
     tabl=tabulate(main, headers=['Account Number','Type','Amount','Date'],tablefmt='fancy_grid')
     print(tabl)
 elif(ch==7):
     sq10='select * from bm;'
     cursor.execute(sq10)
     for i in cursor:
         print(i)
         
 elif(ch==8):
     print('bye')
     break
     
