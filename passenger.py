import mysql.connector as co
import passenger
import os
def passengerdetails():
        while True:
                os.system('cls')
                print("\t\t..........................................")
                print("\t\t**WELCOME TO RAILWAY RESERVATION SYSTEM**")
                print("\t\t...........................................")
                print("\t\t****PASSENGER DETAILS *******")
                print("1: ENTER PASSENGER DETAILS FOR TICKET BOOKING")
                print("2: DISPLAY PASSENGER DETAILS")
                print("3: EXIT")
                print("\t\t =============================================")
                ch=int(input("enter your choice"))
                if(ch==1):
                        passenger.createticket()
                if(ch==2):
                        passenger.displayticket()
                if(ch==3):
                        break
              
def createticket():
                mydb=co.connect(host='localhost',user='root',passwd='1234',database='railway')
                mycursor=mydb.cursor()
                trainno=int(input("Enter train no"))
                pname=input("Enter passenger name")
                age=int(input("Enter passenger age"))
                Gender=input("Enter Gender")
                doj=input("enter date of journey")
                pnr=int(input("enter 10 digit pnr no"))
                fare=int(input("enter fare amount"))
                mycursor.execute("insert into passenger values('"+str(trainno)+"','"+pname+"','"+str(age)+"','"+Gender+"','"+doj+"','"+str(pnr)+"','"+str(fare)+"')")
                mydb.commit()
                mydb.close()
def displayticket():
                mydb=co.connect(host='localhost',user='root',passwd='1234',database='railway')
                mycursor=mydb.cursor()
                trainno=int(input("enter train no"))
                mycursor.execute("select * from passenger where trainno='"+str(trainno)+"'")
                for x in mycursor:
                        print (x)
                        

        
        

        
                
