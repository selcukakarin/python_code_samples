import sqlite3

con=sqlite3.connect("kutuphane.db")
cursor=con.cursor()

def veriAl():
    cursor.execute("Select * from kitaplık")
    liste=cursor.fetchall()     #dönen verimiz liste olarak gelmekte
    print("Kitaplık tablosunun bilgileri")
    for i in liste:
        print(i)

def veriGuncelle(eskiYayinEvi,yeniYayinEvi):
    cursor.execute("update kitaplık set yayinEvi = ? where yayinEvi = ?",(yeniYayinEvi,eskiYayinEvi))
    con.commit()

def veriSil(yazar):
    cursor.execute("delete from kitaplık where yazar=?",(yazar,))
    con.commit()

veriGuncelle("Everest","Metis")
veriSil("Erdil yaşaroğlu")
veriAl()
con.close()