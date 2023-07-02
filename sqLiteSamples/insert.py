import sqlite3

con=sqlite3.connect("kutuphane.db")
cursor=con.cursor()
def veriEkle():
    cursor.execute("insert into kitaplık values('Dönüşüm','Franz Kafka','Everest',76)")
    con.commit()
def veriEkle2(isim,yazar,yayinEvi,sayfaSayisi):
    cursor.execute("insert into kitaplık values(?,?,?,?)",(isim,yazar,yayinEvi,sayfaSayisi))
    con.commit()
# veriEkle()
isim=input("İsim: ")
yazar=input("Yazar: ")
yayinEvi=input("Yayınevi: ")
sayfaSayisi=int(input("Sayfa Sayısı: "))
veriEkle2(isim,yazar,yayinEvi,sayfaSayisi)
con.close()