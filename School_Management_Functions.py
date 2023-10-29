import csv
from clrprint import *
import mysql.connector
from tabulate import tabulate

def add(pw):
    con = mysql.connector.connect(
        host = "localhost",
        user = 'root',
        password = pw ,
        database = 'school')
    cur = con.cursor()
    try :
        cur.execute("create table students (Unique_ID int Primary Key,Admission_No int Not Null unique,Name varchar(50) Not Null,Class Varchar(5),DOB date,Blood_Group Varchar(4),Gender Varchar(8),Father_Name Varchar(50),Mother_Name Varchar(50),Address Varchar(50),Mobile_No bigint Not Null unique,AdhaarCard_No bigint unique)")
    except :
        mysql.connector.errors.ProgrammingError
    n = 1
    fh = open("student-details.csv","a",newline="")
    st = open("student-details.csv","r")
    r = csv.reader(st)
    wr = csv.writer(fh)
    l = []
    for i in r :
        l.append(i)
    s_details = [["UNIQUE ID","ADMISSION NO.","NAME","CLASS","DATE OF BIRTH","BLOOD GROUP","GENDER","FATHER'S NAME","MOTHER'S NAME","ADDRESS","MOBILE NUMBER","ADHAAR CARD NUMBER",]]
    while n > 0 :
        _id = int(input("Student Unique Identification No. : "))
        admission = int(input("Admission Number : "))
        name = input("Name of the Student : ")
        _class = input("Class(In Roman) : ")
        birth = input("Date Of Birth(YYYY-MM-DD) : ")
        blood = input("Blood Group : ")
        gender = input("Gender : ")
        f_name = input("Father's Name : ")
        m_name = input("Mother's Name : ")
        address = input("Address : ")
        mobile = int(input("Mobile Number : "))
        while len(str(mobile)) != 10 :
            clrprint("+-------------------------------------------------------------------+", clr ='red')
            clrprint("|                Mobile Number Must Be Of 10 Digits                 |", clr ='red')
            clrprint("+-------------------------------------------------------------------+", clr ='red')
            mobile = int(input("Re-Enter The Mobile Number : "))
            print("=====================================================================")
        adhaar = int(input("Adhaar Card Number : "))
        while len(str(adhaar)) != 12 :
            clrprint("+-------------------------------------------------------------------+", clr ='red')
            clrprint("|               Adhaar Card Number Must Be Of 12 Digits             |", clr ='red')
            clrprint("+-------------------------------------------------------------------+", clr ='red')
            adhaar = int(input("Re-Enter The Adhaar Card Number : "))
            print("=====================================================================")
        s_list = [_id,admission,name,_class,birth,blood,gender,f_name,m_name,address,mobile,adhaar]
        query = "insert into students values("+str(_id)+","+str(admission)+","+"'"+name+"'"+","+"'"+_class+"'"+","+"'"+birth+"'"+","+"'"+blood+"'"+","+"'"+gender+"'"+","+"'"+f_name+"'"+","+"'"+m_name+"'"+","+"'"+address+"'"+","+str(mobile)+","+str(adhaar)+")"
        cur.execute(query)
        con.commit() 
        s_details.append(s_list)
        print("=====================================================================")
        n = int(input("For Adding More Students Details Press '1' If Not Press '0' : "))
        print("=====================================================================")
    try :
        if "NAME" == l[0][2] :
            s_details.pop(0)
            wr.writerows(s_details)
    except IndexError :
        wr.writerows(s_details)
        fh.close()
    clrprint("+-------------------------------------------------------------------+", clr ='green')
    clrprint("|                  DETAILS ARE ADDED SUCCESFULLY                    |", clr ='green')
    clrprint("+-------------------------------------------------------------------+", clr ='green')

def search():
    st = open("student-details.csv","r")
    r = csv.reader(st)
    n = 1
    l = []
    det = ['Unique ID','Admission Number','Name','Class','Date Of Birth','Blood Group','Gender',"Father's Name","Mother's Name",'Address','Mobile Number','Adhaar Card Number']
    val = 0
    for i in r:
        l.append(i)
    while n>0:
        global _id
        _id = int(input("Enter The Student's Unique Identification No. : "))
        for j in range(1,len(l)) :
            if int(l[j][0]) == _id:
                print("=====================================================================")
                for k in range(0,12):
                    print(det[k],":",l[j][k])
                print("=====================================================================")
                val = 1
                break
            else :
                val = 0
        if val == 0:
            clrprint("+-------------------------------------------------------------------+", clr ='red')
            clrprint("|                         WRONG UNIQUE ID                           |", clr ='red')
            clrprint("+-------------------------------------------------------------------+", clr ='red')
        n = int(input("To Search More Students Details Press '1' If Not Press '0' : "))
        print("=====================================================================")
        
def modify(pw):
    con = mysql.connector.connect(
        host = "localhost",
        user = 'root',
        password = pw ,
        database = 'school')
    cur = con.cursor()
    fh = open("student-details.csv","r")
    r = csv.reader(fh)
    l = []
    n = 1
    m = 1
    q = -1
    for i in r :
        l.append(i)
    det = ['Unique ID','Admission Number','Name','Class','Date Of Birth','Blood Group','Gender',"Father's Name","Mother's Name",'Address','Mobile Number','Adhaar Card Number']
    val = 0
    for i in r:
        l.append(i)
    while n>0:
        global _id
        _id = int(input("Enter Student's Unique Identification No. : "))
        for j in range(1,len(l)) :
            if int(l[j][0]) == _id:
                print("=====================================================================")
                for k in range(0,12):
                    print(det[k],":",l[j][k])
                print("=====================================================================")
                val = 1
                n = 0
                break
            else :
                val = 0
        if val == 0:
            clrprint("+-------------------------------------------------------------------+", clr ='red')
            clrprint("|                         WRONG UNIQUE ID                           |", clr ='red')
            clrprint("+-------------------------------------------------------------------+", clr ='red')
    for j in range(0,len(l)):
            if str(_id) in l[j]:
                q = j
                exit
    if q>=0:
        while m>0:
            print("What You Want To Modify")
            print('''+-----------+------------------+--------------------+
| Unique_id |   Admission_No   |        Name        |
+-----------+------------------+--------------------+
|   Class   |   Date_Of_Birth  |    Blood_Group     |
+-----------+------------------+--------------------+
|  Gender   |   Father_Name    |   Mother's Name    |
+-----------+------------------+--------------------+
|  Address  |     Mobile_No    |   AdhaarCard_No    |
+-----------+------------------+--------------------+''')
            print("=====================================================================")
            a = input("Enter Exact Words From Above Table: ")
            v = ['unique_id','admission_no','name','class','date_of_birth','blood_group','gender',"father_name","mother_name",'address','mobile_no','adhaarcard_no']
            if a.lower() in v :
                if a.lower() == "unique_id":
                    print("=====================================================================")
                    l[q][0] = input("Enter New unique id : ")
                    print("=====================================================================")
                    query = "update students set "+a+" = "+l[q][0]+" where Unique_ID = "+str(_id)
                    cur.execute(query)
                    con.commit()
                elif a.lower() == "admission_no":
                    print("=====================================================================")
                    l[q][1] = input("Enter New Admission Number : ")
                    print("=====================================================================")
                    query = "update students set "+a+" = "+l[q][1]+" where Unique_ID = "+str(_id)
                    cur.execute(query)
                    con.commit()
                elif a.lower() == "name":
                    print("=====================================================================")
                    l[q][2] = input("Enter New Name : ")
                    print("=====================================================================")
                    query = "update students set "+a+" = "+"'"+l[q][2]+"'"+" where Unique_ID = "+str(_id)
                    cur.execute(query)
                    con.commit()
                elif a.lower() == "class":
                    print("=====================================================================")
                    l[q][3] = input("Enter New class : ")
                    print("=====================================================================")
                    query = "update students set "+a+" = "+"'"+l[q][2]+"'"+" where Unique_ID = "+str(_id)
                    cur.execute(query)
                    con.commit()
                elif a.lower() == "date_of_birth":
                    print("=====================================================================")
                    l[q][4] = input("Enter New Date Of Birth : ")
                    print("=====================================================================")
                    query = "update students set "+a+" = "+"'"+l[q][2]+"'"+" where Unique_ID = "+str(_id)
                    cur.execute(query)
                    con.commit()
                elif a.lower() == "blood_group":
                    print("=====================================================================")
                    l[q][5] = input("Enter New Blood Group : ")
                    print("=====================================================================")
                    query = "update students set "+a+" = "+"'"+l[q][2]+"'"+" where Unique_ID = "+str(_id)
                    cur.execute(query)
                    con.commit()
                elif a.lower() == "gender":
                    print("=====================================================================")
                    l[q][6] = input("Enter New Gender : ")
                    print("=====================================================================")
                    query = "update students set "+a+" = "+"'"+l[q][2]+"'"+" where Unique_ID = "+str(_id)
                    cur.execute(query)
                    con.commit()
                elif a.lower() == "father_name":
                    print("=====================================================================")
                    l[q][7] = input("Enter New Name Of Father : ")
                    print("=====================================================================")
                    query = "update students set "+a+" = "+"'"+l[q][2]+"'"+" where Unique_ID = "+str(_id)
                    cur.execute(query)
                    con.commit()
                elif a.lower() == "mother_name":
                    print("=====================================================================")
                    l[q][8] = input("Enter New Name Of Mother : ")
                    print("=====================================================================")
                elif a.lower() == "address":
                    print("=====================================================================")
                    l[q][9] = input("Enter New Address : ")
                    print("=====================================================================")
                    query = "update students set "+a+" = "+"'"+l[q][2]+"'"+" where Unique_ID = "+str(_id)
                    cur.execute(query)
                    con.commit()
                elif a.lower() == "mobile_no":
                    print("=====================================================================")
                    l[q][10] = int(input("Enter New Mobile Number : "))
                    print("=====================================================================")
                    while len(str((l[q][10]))) != 10 :
                        clrprint("+-------------------------------------------------------------------+", clr ='red')
                        clrprint("|                Mobile Number Must Be Of 10 Digits                 |", clr ='red')
                        clrprint("+-------------------------------------------------------------------+", clr ='red')
                        l[q][10] = int(input("Re-Enter The Mobile Number : "))
                        print("=====================================================================")
                    query = "update students set "+a+" = "+l[q][0]+" where Unique_ID = "+str(_id)
                    cur.execute(query)
                    con.commit()
                elif a.lower() == "adhaarcard_no":
                    print("=====================================================================")
                    l[q][11] = int(input("Enter New Adhaar Card Number : "))
                    print("=====================================================================")
                    while len(str((l[q][11]))) != 12 :
                        clrprint("+-------------------------------------------------------------------+", clr ='red')
                        clrprint("|               Adhaar Card Number Must Be Of 12 Digits             |", clr ='red')
                        clrprint("+-------------------------------------------------------------------+", clr ='red')
                        l[q][11] = int(input("Re-Enter The Adhaar Card Number : "))
                        print("=====================================================================")
                    query = "update students set "+a+" = "+l[q][0]+" where Unique_ID = "+str(_id)
                    cur.execute(query)
                    con.commit()
                m = int(input("To Modify More Details Of This Student Press '1' If Not Press '0' : "))
            else :
                clrprint("=====================================================================", clr ='red')
                clrprint("                           WRONG HEADING                             ", clr ='red')
                clrprint("=====================================================================", clr ='red')
                
    else:
        print("Wrong Unique ID")
    fh.close()
    clrprint("=====================================================================", clr='green')
    clrprint("                 DETAILS ARE MODIFIED SUCCESSFULLY                   ", clr='green')
    clrprint("=====================================================================", clr='green')
    st = open("student-details.csv","w",newline="")
    wr = csv.writer(st)
    wr.writerows(l)
    st.close()


def delete(pw):
    con = mysql.connector.connect(
        host = "localhost",
        user = 'root',
        password = pw ,
        database = 'school')
    cur = con.cursor()
    fh = open("student-details.csv","r")
    wr = csv.reader(fh)
    l = []
    for i in wr:
        l.append(i)
    n = 1
    det = ['Unique ID','Admission Number','Name','Class','Date Of Birth','Blood Group','Gender',"Father's Name","Mother's Name",'Address','Mobile Number','Adhaar Card Number']
    val = 0
    while n>0:
        global _id
        _id = int(input("Enter The Student's Unique Identification No. : "))
        for j in range(1,len(l)) :
            if int(l[j][0]) == _id:
                print("=====================================================================")
                for k in range(0,12):
                    print(det[k],":",l[j][k])
                print("=====================================================================")
                val = 1
                n = 0
                break
            else :
                val = 0
        if val == 0:
            clrprint("+-------------------------------------------------------------------+", clr ='red')
            clrprint("|                         WRONG UNIQUE ID                           |", clr ='red')
            clrprint("+-------------------------------------------------------------------+", clr ='red')
    p = int(input("To Delete All The Details Press '1' : "))
    fh.close()
    cur.execute("delete from students where Unique_id = "+str(_id))
    con.commit()
    if p == 1 :
        l.pop(j)
        clrprint("=====================================================================", clr='green')
        clrprint("                        DElETED SUCCESSFULLY                         ", clr='green')
        clrprint("=====================================================================", clr='green')

        st = open("student-details.csv","w",newline="")
        r = csv.writer(st)
        r.writerows(l)
        st.close()


def cl_details(pw):
    con = mysql.connector.connect(
        host = "localhost",
        user = 'root',
        password = pw ,
        database = 'school')
    cur = con.cursor()
    n = 1
    while n>0:
        cl = input("Enter The Class For details In Roman : ")
        query = "select * from students where Class = "+"'"+cl+"'"+" Order by Name"
        cur.execute(query)
        data = cur.fetchall()
        header = ["Unique_ID","Admission_No","Name","Class","DOB","Blood_Group","Gender","Father_Name","Mother_Name","Address","Mobile_No","AdhaarCard_No"]
        clrprint(tabulate(data,headers = header,tablefmt = "grid"), clr = 'green')
        n = int(input("For More Classes Details Press 1 If Not Press 0 : "))

    

