import mysql.connector as co
import train
import os
def traindetails():
        while True:
                os.system('cls')
                print("#"*80)
                print("\t\t**WELCOME TO RAILWAY RESERVATION SYSTEM**")
                print("#"*80)
                print("\t\t****TRAIN DETAILS *******")
                print("1: ENTER NEW TRAIN")
                print("2: DISPLAY TRAIN DETAILS")
                print("3: REMOVE TRAIN")
                print("4: EXIT")
                print("\t\t =============================================")
                ch=int(input("enter your choice"))
                if(ch==1):
                        train.createtrain()
                elif(ch==2):
                        train.displaytrain()
                elif(ch==3):
                        train.removetrain()
                if(ch==4):
                        break
              
def createtrain():
                mydb=co.connect(host='localhost',user='root',passwd='1234',database='railway')
                mycursor=mydb.cursor()
                trainno=int(input("Enter train no"))
                trainname=input("Enter train name")
                start=input("Enter source station name")
                stop=input("Enter destination station name")
                mycursor.execute("insert into train values('"+str(trainno)+"','"+trainname+"','"+start+"','"+stop+"')")
                mydb.commit()
                mydb.close()
def displaytrain():
                mydb=co.connect(host='localhost',user='root',passwd='1234',database='railway')
                mycursor=mydb.cursor()
                trainno=int(input("enter train no"))
                mycursor.execute("select * from train where trainno='"+str(trainno)+"'")
                print("="*80)
                print("Train no|Train Name|tStart|tStop")
                for x in mycursor:
                        print (x)
                print("="*80)
                        
def removetrain():
                mydb=co.connect(host='localhost',user='root',passwd='1234',database='railway')
                mycursor=mydb.cursor()
                trainno=int(input("enter train no"))
                mycursor.execute("delete from train where trainno='"+str(trainno)+"'")
                mydb.commit()
        
        

        
                
