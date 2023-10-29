from School_Management_Functions import *
from clrprint import *

a = 1
s = 1
print("=====================================================================")
pw = input("Enter The Password : ")
print("=====================================================================")
while s>0:
    try :
        con = mysql.connector.connect(
            host = "localhost",
            user = 'root',
            password = pw,auth_plugin='mysql_native_password',
            database = 'school')
        s = 0
    except mysql.connector.errors.ProgrammingError:
        clrprint("+-------------------------------------------------------------------+", clr ='red')
        clrprint("|                          WRONG PASSWORD                           |", clr ='red')
        clrprint("+-------------------------------------------------------------------+", clr ='red')
        print("=====================================================================")
        pw = input("Re-Enter The Password : ")
        print("=====================================================================")
while a>0:
    print("=====================================================================")
    print("To Add Students Details Press         -       1")
    print("To Search Students Details Press      -       2")
    print("To Search Class Details Press         -       3")
    print("To Modify Students Details Press      -       4")
    print("To Delete Students Details Press      -       5")
    print("To Close The Program Press            -       0")
    print("=====================================================================")
    a = int(input("Enter Here : " ))
    print("=====================================================================")
    if a == 1 :
        add(pw)
    elif a == 2 :
        search()
    elif a == 3 :
        cl_details(pw)
    elif a == 4 :
        modify(pw)
    elif a == 5 :
        delete(pw)
    elif a != 0 :
        clrprint("=====================================================================", clr ='red')
        clrprint("                               WRONG CODE                            ", clr ='red')
        clrprint("=====================================================================", clr ='red')
clrprint("=====================================================================", clr ='green')
clrprint("                         PROGRAM CLOSED                              ", clr ='green')
clrprint("=====================================================================", clr ='green')
