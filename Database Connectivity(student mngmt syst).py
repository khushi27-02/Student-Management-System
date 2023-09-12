import sys
import sqlite3 as sql
con = sql.connect("studentDB")
cursor = con.cursor()
cursor.execute("create table if not exists studentinfo(sid int primary key,name varchar(50) not null,email varchar(40) not null, dob date,phone bigint,address varchar(300))")
con.commit()               
def InsertData():
    sid = int(input("Enter Student ID: "))
    name = input("Enter Name: ")
    email = input("Enter email: ")
    dob = input("Enter DOB(YYYY-MM-DD): ")
    phone = int(input("Enter phone no: "))
    address = input("Enter address: ")
    qry = "insert into studentinfo values(%d,'%s','%s','%s',%d,'%s')"%(sid,name,email,dob,phone,address)
    cursor.execute(qry)
    con.commit()
    if cursor.rowcount>0:
        print("\nRecord Inserted")
    else:
        print("\nError in inserting the record")
    input("\n\nPress Enter To Continue")
    
def DisplayAll():
    qry = "select * from studentinfo order by name asc"
    cursor.execute(qry)
    result = cursor.fetchall()
    if len(result)>0:
        print("_"*94)
        print("%5s %20s %20s %12s %12s %20s"%("Sid", "Name", "Email", "DOB", "Phone no.", "Address"))
        print("_"*94)
        for row in result:
            print("%5d %20s %20s %12s %12d %20s"%(row[0],row[1],row[2],row[3],row[4],row[5]))
    else:
        print("No Record Found!!")
    input("\n\nPress Enter To Continue")
    
def DisplayById():
    id = int(input("Enter Student Id: "))
    qry = "select * from studentinfo where sid ="+ str(id)
    cursor.execute(qry)
    row = cursor.fetchone()
    if row:
        print("_"*94)
        print("%5s %20s %20s %12s %12s %20s"%("Sid", "Name", "Email", "DOB", "Phone no.", "Address"))
        print("_"*94)
        print("%5d %20s %20s %12s %12d %20s"%(row[0],row[1],row[2],row[3],row[4],row[5]))
    else:
        print("No Record Found!!")
    input("\n\nPress Enter To Continue")
    
def DisplayByName():
    name = input("Enter name: ")
    qry = "select * from studentinfo where name ='%s'"%(name)
    cursor.execute(qry)
    result = cursor.fetchall()
    if len(result)>0:
        print("_"*94)
        print("%5s %20s %20s %12s %12s %20s"%("Sid", "Name", "Email", "DOB", "Phone no.", "Address"))
        print("_"*94)
        for row in result:
            print("%5d %20s %20s %12s %12d %20s"%(row[0],row[1],row[2],row[3],row[4],row[5]))
    else:
        print("No Record Found!!")
    input("\n\nPress Enter To Continue")
    
def EditRecord():
    id = int(input("Enter Student Id: "))
    cursor.execute("select * from studentinfo where sid=" +str(id))
    result = cursor.fetchall()
    if len(result) > 0:
        while True:
            print("Press 1 to update name")
            print("Press 2 to update email")
            print("Press 3 to update dob")
            print("Press 4 to update phone no")
            print("Press 5 to update address")
            print("Press 6 to update all")
            print("Enter 7 to Back")
            ch = int(input("Enter Choice: "))
            if ch == 1:
                name = input("Enter Name: ")
                cursor.execute("update studentinfo set name='"+name+"' where sid = "+str(id))
                con.commit()
                if cursor.rowcount > 0:
                    print("Record Updating Successfully")
                else:
                    print("Error in updating the record")
            elif ch == 2:
                email = input("Enter email: ")
                cursor.execute("update studentinfo set email='"+email+"' where sid = "+str(id))
                con.commit()
                if cursor.rowcount > 0:
                    print("Record Updating Successfully")
                else:
                    print("Error in updating the record")
            elif ch == 3:
                dob = input("Enter dob: ")
                cursor.execute("update studentinfo set dob='"+dob+"' where sid = "+str(id))
                con.commit()
                if cursor.rowcount > 0:
                    print("Record Updating Successfully")
                else:
                    print("Error in updating the record")
            elif ch == 4:
                phone = int(input("Enter phone no: "))
                cursor.execute("update studentinfo set phone ='"+phone+"' where sid = "+str(id))
                con.commit()
                if cursor.rowcount > 0:
                    print("Record Updating Successfully")
                else:
                    print("Error in updating the record")
            elif ch == 5:
                address = input("Enter address: ")
                cursor.execute("update studentinfo set address='"+address+"' where sid = "+str(id))
                con.commit()
                if cursor.rowcount > 0:
                    print("Record Updating Successfully")
                else:
                    print("Error in updating the record")
            elif ch == 6:
                name = input("Enter Name: ")
                email = input("Enter email: ")
                dob = input("Enter dob: ")
                phone = int(input("Enter phone no: "))
                address = input("Enter address: ")
                qry = "update studentinfo set name='%s',email='%s',dob='%s',phone='%d',address='%s' where sid = '%d'"%(name,email,dob,phone,address,id)
                cursor.execute(qry)
                con.commit()
                if cursor.rowcount > 0:
                    print("Record Updating Successfully")
                else:
                    print("Error in updating the record")
            elif ch == 7:
                break
            else:
                print("Invalid Choice...")
            input("\n\nPress Enter To Continue")
    else:
        print("Student Id not found!!")
    input("\n\nPress Enter To Continue")    
        
def DeleteAllRecord():
    cursor.execute("delete from studentinfo")
    con.commit()
    if cursor.rowcount > 0:
        print("All Record Deleted")
    else:
        print("Table is already empty!!")
    input("\n\nPress Enter To Continue")
    
def DeleteRecordById ():
    id = int(input("Enter Student Id: "))
    cursor.execute("delete from studentinfo where sid="+str(id))
    con.commit()
    if cursor.rowcount > 0:
        print("Record Deleted!!")
    else:
        print("Student Id not exist!!")
    input("\n\nPress Enter To Continue")    

while True:
    print("1 Insert Student Record")
    print("2 Display All Student Record")
    print("3 Display Student Record By Id")
    print("4 Display Student record By Name")
    print("5 Edit Student Record")
    print("6 Delete All Student Record")
    print("7 Delete Student Record By Id")
    print("8 Exit")
    choice = int(input("Enter Choice: "))
    if choice == 1:
        InsertData()
    elif choice == 2:
        DisplayAll()
    elif choice == 3:
        DisplayById()
    elif choice == 4:
        DisplayByName()
    elif choice == 5:
        EditRecord()
    elif choice == 6:
        DeleteAllRecord()
    elif choice == 7:
        DeleteRecordById()
    elif choice == 8:
        sys.exit()
    else:
        print("Invalid Choice\n\nEnter Again.....\n")
