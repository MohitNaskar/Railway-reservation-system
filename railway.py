import train
import passenger
import cancel
import graph
import os
while True:
        os.system("cls")
        print("#"*80)
        print("\t\t**WELCOME TO RAILWAY RESERVATION SYSTEM**")
        print("#"*80)
        print("1: TRAIN DETAILS")
        print("2: PASSENGER AND TICKET DETAILS")
        print("3: CANCELLATION DETAILS")
        print("4: GRAPHICAL PRESENTATION")
        print("5: EXIT")
        print("\t\t =============================================")
        ch=int(input("enter your choice"))
        if(ch==1):
                train.traindetails()
        elif(ch==2):
                passenger.passengerdetails()
        elif(ch==3):
                cancel.canceldetails()
        elif(ch==4):
                graph.graphical()
        elif(ch==5):
                break
        else:
                print("wrong choice/Try again")
                ans=input("want to continue")
                
                
