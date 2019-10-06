import sqlite3

con=sqlite3.connect("kutuphane.db")
cursor=con.cursor()

def veriAl():
    cursor.execute("Select * from kitaplık")
    liste=cursor.fetchall()     #dönen verimiz liste olarak gelmekte
    print("Kitaplık tablosunun bilgileri")
    for i in liste:
        print(i)

def veriAl2():
    cursor.execute("select isim,yazar from kitaplık")
    liste=cursor.fetchall()
    print("Kitaplık tablosunun bilgileri")
    for i in liste:
        print(i)

def veriAl3(yayinEvi):
    cursor.execute("select * from kitaplık where yayinEvi = ?",(yayinEvi,))
    liste=cursor.fetchall()
    print("Kitaplık tablosunun bilgileri")
    for i in liste:
        print(i)

veriAl()
veriAl2()
veriAl3("Everest")
