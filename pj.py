from tabulate import tabulate
import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="1234", database="ppj")


def insert(NAME, AGE, PLACE):
    res = con.cursor()
    sql = "insert into users (name,age,place) values (%s,%s,%s)"
    user = (name, AGE, PLACE)
    res.execute(sql, user)
    con.commit()
    print("Data Insert Success")


def update(Name, AGE, PLACE, ID):
    res = con.cursor()
    sql = "update users set NAME =%s,AGE =%s,PLACE =%s where ID =%s"
    user = (Name, AGE, PLACE, ID)
    res.execute(sql, user)
    con.commit()
    print("Data Update Success")



def select():
    res = con.cursor()
    sql = "SELECT ID,NAME,AGE,PLACE from users"
    res.execute(sql)
    # result=res.fetchone()
    # result=res.fetchmany(2)
    result = res.fetchall()
    print(tabulate(result, headers=["ID", "NAME", "AGE", "Place"]))


def delete(ID):
    res = con.cursor()
    sql = "delete from users where ID=%s"
    user = (ID,)
    res.execute(sql, user)
    con.commit()
    print("Data Delete Success")



while True:
    print("1.Insert Data")
    print("2.Update Data")
    print("3.Select Data")
    print("4.Delete Data")
    print("5.Exit")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        name = input("Enter Name : ")
        age = input("Enter Age : ")
        place = input("Enter Place : ")
        insert(name, age, place)
    elif choice == 2:
        id = input("Enter The Id : ")
        name = input("Enter Name : ")
        age = input("Enter Age : ")
        place = input("Enter Place : ")
        update(name, age, place, id)
    elif choice == 3:
        select()
    elif choice == 4:
        id = input("Enter The Id to Delete : ")
        delete(id)
    elif choice == 5:
        quit()
    else:
        print("Invalid Selection . Please Try Again !")