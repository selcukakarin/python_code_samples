from kutuphane import *

print("""
******************************************
Kütüphane programına hoşgeldin

İşlemler;

1. Kitapları göster

2. Kitap sorgula

3. Kitap ekle

4. Kitap sil

5. Baskı yükselt

Çıkmak için q'ya basın
******************************************
""")

kutuphane=Kutuphane()

while(True):
    islem=input("Yapılacak işlem: ")

    if(islem=="q"):
        print("program sonlandırılıyor.....")
        break
    elif(islem=="1"):
        kutuphane.kitaplariGoster()
    elif(islem=="2"):
        isim=input("Hangi kitabı aramak istiyorsunuz? : ")
        print("Kitap sorgulanıyor... ")
        time.sleep(2)
        kutuphane.kitapSorgula(isim)
    elif(islem=="3"):
        isim=input("Eklenecek olan kitabın ismi : ")
        yazar=input("Eklenecek olan kitabın yazarı : ")
        yayinevi=input("Eklenecek olan kitabın yayinevi : ")
        tur=input("Eklenecek olan kitabın türü : ")
        baski=input("Eklenecek olan kitabın baskı sayısı : ")
        yeniKitap=Kitap(isim,yazar,yayinevi,tur,baski)
        print("Kitap ekleniyor....")
        time.sleep(2)
        kutuphane.kitapEkle(yeniKitap)
        print("Kitap eklendi.")
    elif(islem=="4"):
        isim=input("Hangi kitabı silmek istiyorsunuz? ")
        cevap=input("Emin misiniz? (e/h) ")
        if cevap=="e":
            print("Kitap siliniyor")
            time.sleep(2)
            kutuphane.kitapSil(isim)
            print("Kitap silindi.")
        
    elif(islem=="5"):
        isim=input("Hangi kitabın baskısını yükseltmek istersiniz? ")
        print("Baskı yükseltiliyor...")
        time.sleep(2)
        kutuphane.baskiYukselt(isim)
        print("Baskı yükseltildi.")
    else:
        print("Geçersiz işlem.")