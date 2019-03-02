import random
import msvcrt

class Kumanda():
    def __init__(self,tvDurum="Kapalı",tvSes=0,kanalListesi=["Trt"],kanal="Trt"):
        print("Kumanda Oluşturuluyor...")

        self.tvSes=tvSes
        self.tvDurum=tvDurum
        self.kanalListesi=kanalListesi
        self.kanal=kanal

    def sesiAzaltArttir(self):
        while True:
            karakter =input("Azaltmak için '<'e bas\nArttırmak için '>'e bas\nTamam ise'q ya bas\n")
            
            if(karakter=="<"):
                if(self.tvSes!=0):
                    self.tvSes-=1
                    print("Ses: ",self.tvSes)
                else:
                    print("0'dan daha aşağıya inemeyiz...")
            elif(karakter==">"):
                    if(self.tvSes!=32):
                        self.tvSes+=1
                        print("Ses: ",self.tvSes)
                    else:
                        print("32'den daha üste çıkamayız....")
            else:
                 print("Ses Güncellendi: ",self.tvSes)
                 break
    def tvKapat(self):
        if(self.tvDurum=="Kapalı"):
            print("Tv zaten kapalı")
        else:
            print("Tv kapatılıyor.")
            self.tvDurum="Kapalı"
    def tvAc(self):
        if(self.tvDurum=="Açık"):
            print("Tv zaten açık")
        else:
            print("Tv açılıyor")
            self.tvDurum="Açık"
    def __str__(self):
        return "TV durumu : {}\nSes: {}\nKanallar: {}\nŞu anki kanal: {}\n".format(self.tvDurum,self.tvSes,self.kanalListesi,self.kanal)
    def __len__(self):
        return len(self.kanalListesi)
    def rastgeleKanal(self):
        rastgele=random.randint(0,len(self.kanalListesi)-1)
        self.kanal=self.kanalListesi[rastgele]
        print("Şu anki Kanal : ",self.kanal)
    def kanalEkle(self,kanal):
        print("Kanal ekleniyor... ")
        self.kanalListesi.append(kanal)

kumanda=Kumanda()
print("""
********************************

Televizyon Uygulaması

İşlemler;

1.Televizyonu Aç

2.Televizyonu Kapat

3.Televizyon Bilgileri

4.Kanal Sayısını Öğrenme

5.Kanal Ekle

6.Rastgele Kanala Geç

7.Sesi Azalt ya da Arttır

Çıkmak için q'ya basın

********************************
""")

while True:
    islem=input("İşlem seçiniz: ")
    if(islem=="q"):
        print("Programdan çıkılıyor....")
        break
    if(islem=="1"):
        kumanda.tvAc()
    elif(islem=="2"):
        kumanda.tvKapat()
    elif(islem=="3"):
        print(kumanda)
    elif(islem=="4"):
        print("Kanal Sayısı: ",len(kumanda))
    elif(islem=="5"):
        kanallar=input("Eklemek istediğiniz kanalları ',' ile ayırarak giriniz: ")
        eklenecekler=kanallar.split(",")
        for i in eklenecekler:
            kumanda.kanalEkle(i)
        print("Kanal Listesi Başarıyla Güncellendi.")
    elif(islem=="6"):
        kumanda.rastgeleKanal()
    elif(islem=="7"):
        kumanda.sesiAzaltArttir()
    else:
        print("Geçersiz işlem")