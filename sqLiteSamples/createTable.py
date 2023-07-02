import sqlite3

con=sqlite3.connect("kutuphane.db")     #var ise kutuphane.db ye baglan yoksa olustur
cursor=con.cursor()
def tabloOlustur():
    cursor.execute("create table if not exists kitaplık(isim text,yazar text,yayinEvi text,sayfaSayisi int)")
    con.commit()        #sql çalıştır
tabloOlustur()

con.close()