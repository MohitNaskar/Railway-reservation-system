import  mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='1234',database='railway')
cur = conn.cursor()
#cur.execute('create table user_table(username varchar(25) primary key,passwrd varchar(25) not null )')
print('====================WELCOME RAILWAY RESERVATION SYSTEM==================')
print(' =======   ||======            |           /\      =====\       /\      |   /  |    |')
print('||     ||  ||                  |          /  \     |     |     /  \     |  /   |    |')
print('||     ||  ||=====    =======  |         /----\    |     |    /----\    | /    |----|')
print('||     ||  ||                  |        /      \   |     |   /      \   | \    |    |')
print('||     ||  ||                  |     | /        \  |     |  /        \  |  \   |    |')
print('  ======                        -----|             |====/  /          \ |   \  |    |')
import datetime as dt
print(dt.datetime.now())
print('\t\t\t1.REGISTER')
print()
print('\t\t\t2.LOGIN')
print()



n=int(input('enter your choice='))
print()

if n== 1:
     name=input('Enter a Username=')
     print()
     passwd=int(input('Enter a 4 DIGIT Password='))
     print()
     V_SQLInsert="INSERT  INTO user_table (passwrd,username) values (" +  str (passwd) + ",' " + name + " ') "
     cur.execute(V_SQLInsert)
     conn.commit()
     print()
     print('USER created succesfully')
     import railway

if  n==2 :
    while True:
        name=input('Enter your Username=')
        print()
        passwd=int(input('Enter your 4 DIGIT Password='))
        V_Sql_Sel="select * from user_table where passwrd='"+str (passwd)+"' and username=  ' " +name+ " ' "
        cur.execute(V_Sql_Sel)
        if cur.fetchone() is  None:
            print()
            print('Invalid username or password')
            ans=input("want to continue")
        else:
            print()
            import railway
     
