import mysql.connector as co
import os
import cancel
def canceldetails():
        while True:
                print("\t\t..........................................")
                print("\t\t**WELCOME TO RAILWAY RESERVATION SYSTEM**")
                print("\t\t...........................................")
                print("\t\t****CANCELLATION DETAILS *******")
                print("1: CANCEL TICKET")
                print("2: REFUND DETAILS")
                print("3: EXIT")
                print("\t\t =============================================")
                ch=int(input("enter your choice"))
                if(ch==1):
                        cancel.cancelticket()
                if(ch==2):
                        cancel.displayticket()
                if(ch==3):
                        break
              
def cancelticket():
                mydb=co.connect(host='localhost',user='root',passwd='1234',database='railway')
                mycursor=mydb.cursor()
                trainno=int(input("Enter train no"))
                pnr=int(input("enter 10 digit pnr no"))
                fare=int(input("enter the fare amount"))
                mycursor.execute("insert into cancel values('"+str(trainno)+"','"+str(pnr)+"','"+str(refund)+"'")
                mydb.commit()
                mydb.close()
def displayticket():
                mydb=co.connect(host='localhost',user='root',passwd='1234',database='railway')
                mycursor=mydb.cursor()
                trainno=int(input("enter train no"))
                mycursor.execute("select * from cancel where trainno='"+str(trainno)+"'")
                for x in mycursor:
                        print (x)

        
        

                        
