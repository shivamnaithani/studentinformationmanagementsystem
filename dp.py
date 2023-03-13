#program of student information management system

#creating database
import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root",passwd='root')
mycursor=mydb.cursor()
mycursor.execute("create database if not exists student")


#creating table
import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root",passwd='root',database='student')
mycursor=mydb.cursor()
mycursor.execute("create table if not exists SIMS(admn_no int(8) primary key,name char(16), fname char(16),DOB DATE,\
                                 class int(2), section char(1))")


#user-defined functions
def add():
     import mysql.connector
     try:
          mydb=mysql.connector.connect(host="localhost", user="root",passwd='root',database='student')
          mycursor=mydb.cursor()
          admn=int(input("ENTER ADMISSION NO="))
          while(1):
            name=input("ENTER NAME=").lower()
            fname=input("ENTER FATHER'S NAME=").lower()
            if (name.isalpha() and fname.isalpha()):
                break
            else:
                print('Only enter alphabets')
        
          
          dob=input("ENTER DATE OF BIRTH(Y/M/D)=")
          cls=int(input("ENTER CLASS="))
          sn=input("ENTER SECTION=").lower()
          sql = "insert into sims (admn_no ,name, fname ,DOB,class,section) values('%d','%s','%s','%s','%d','%s')" %(admn,name,fname,dob,cls,sn)
          mycursor.execute(sql)
          mydb.commit()
          print("Record Inserted!")
     except Exception as e:
          print(e)


def display():
     print()
     import mysql.connector
     mydb=mysql.connector.connect(host="localhost", user="root",passwd='root',database='student')
     mycursor=mydb.cursor()
     mycursor.execute("select * from sims")
     print("\t DETAILED STUDENT TABLE".center(100))
     print( "-"*120)
     print("ADMNO\t\t  ","NAME\t\t  ","FNAME\t\t  ","DATE OF BIRTH  ","CLASS  ","SECTION")
     print("-"*120)
     for x in mycursor:
          a = x[0]
          c = dict()
          ch = 'y'
          b = (x)
          c[a] = b
          l = c.keys()
          for i in l:
               print("-"*120)
               q = c[i]
               for j in q:
                   if(len(str(j)) == 1 and len(str(j)) == 2):
                       print(j,end="\t")
                   elif (type(j) == str and len(j) <9):
                       print(j,end="\t\t    ") 
                   else:
                       print(j,end="\t     ")                        
               print()
               print("-"*120)
               break;        

def update():
     import mysql.connector
     try:
          mydb=mysql.connector.connect(host="localhost", user="root",passwd='root',database='student')
          mycursor=mydb.cursor()
          n=int(input("ENTER ADMISSION NO="))
          name=input("ENTER NAME=").lower()
          fname=input("ENTER FATHER'S NAME=").lower()
          dob=input("ENTER DATE OF BIRTH(Y/M/D)=")
          cls=int(input("ENTER CLASS="))
          sn=input("ENTER SECTION=").lower() 
          ab="update sims set  name='%s',fname='%s' ,dob='%s',class='%d',section='%c' where admn_no='%d' " %(name,fname,dob,cls,sn,n)
          mycursor.execute(ab)
          mydb.commit()
          print("Record Updated!")       
     except Exception as e:
          print(e)



def search():
     import mysql.connector
     try:
          mydb=mysql.connector.connect(host="localhost", user="root",passwd='root',database='student')
          mycursor=mydb.cursor()
          print("NOTE : IF ADMISSION NUMBER NOT AVAILABLE THEN IT SHOWS NOTHING \
OTHERWISE SHOWS SUCCESSFUL")
          n=int(input("ENTER ADMISSION NUMBER="))
          mycursor.execute("select * from sims where admn_no= '%d' " %(n) )
     except Exception as e:
          print(e)
     print()
     for x in mycursor:
          a = x[0]
          c = dict()
          b = (x)
          c[a] = b
          l = c.keys()
          for i in l:
               print("SEARCH SUCCESSFUL")
               print("\nADMISSION NO-",i,":")
               print("-"*120)
               q = c[i]
               print("ADMNO\t\t  ","NAME\t\t  ","FNAME\t\t  ","DATE OF BIRTH  ","CLASS  ","SECTION")
               print("-"*120)
               print("-"*120)
          for j in q:
                   if (type(j) == str and len(j) <9):
                       print(j,end="\t\t   ")
                   else:
                       print(j,end="\t   ")                        
          print()
          print("-"*120)
          break;
          
     
def delete():
     import mysql.connector
     try:
          mydb=mysql.connector.connect(host="localhost", user="root",passwd='root',database='student')
          mycursor=mydb.cursor()
          d=int(input("ENTER ADMISSION NUMBER="))
          mycursor.execute("delete from sims where admn_no= '%d' " %(d) )
          mydb.commit()
          print("Record Deleted!")
     except Exception as e:
          print(e)

#homepage program       
ch="Y"
while ch =="Y" :
     print( " "*50 ,"-"*79)
     print("STUDENT INFORMATION MANAGEMENT SYSTEM".center(180))
     print( " "*50 ,"-"*79)
     print()
     print()
     print("1)ADD RECORD")
     print("2)DISPLAY TABLE")
     print("3)UPDATE RECORD")
     print("4)SEARCH RECORD")
     print("5)DELETE RECORD")
     print("6)EXIT")
     c=int(input("Enter your choice :"))
     print()
     if c == 1:
        add()
     elif c == 3:
        update()
     elif c==2:
        display()
     elif c==4:
        search()
     elif c ==5:
        delete()
     elif c ==6:
          break;
     print()
     n = input("press any key to continue....")
