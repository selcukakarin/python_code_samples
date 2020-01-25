import random
import time
class Kumanda():
    def __init__(self,tvDurum = "Kapalı",tvSes = 0, kanalListesi = ["Trt"],kanal = "Trt"):
        self.tvDurum = tvDurum
        self.tvSes = tvSes
        self.kanalListesi = kanalListesi
        self.kanal = kanal
    def tvAc(self):
        if(self.tvDurum == "Açık"):
            print("Tv zaten açık")
        else:
            self.tvDurum = "Açık"
            print("Tv açılıyor")
            time.sleep(1)
            print("Tv açıldı.")
    def tvKapat(self):
        if(self.tvDurum == "Kapalı"):
            print("Tv zaten kapalı")
        else:
            self.tvDurum = "Kapalı"
            print("Tv kapanıyor")
            time.sleep(1)
            print("Tv kapandı.")
    def sesAyarlari(self):
        if self.tvDurum == "Açık":
            while True:
                cevap = input("Ses azaltmak için '<', ses arttırmak için '>', çıkmak için 'çıkış' yazın")
                if(cevap == "çıkış"):
                    print("Ses menüsünden çıkılıyor..")
                    time.sleep(1)
                    print("Ses menüsünden çıkıldı.")
                    break
                elif(cevap == "<"):
                    if(self.tvSes == 0):
                        print("Ses daha fazla azaltılamaz")
                    else:
                        self.tvSes -= 1
                elif(cevap == ">"):
                    if(self.tvSes == 30):
                        print("Ses daha fazla arttırılamaz")
                    else:
                        self.tvSes += 1
                print("Ses düzeyi : ",self.tvSes)
        else:
            print("Ses açma işlemi tv durumu kapalı olduğu için yapılamamaktadır.")
    def kanalEkle(self,kanalIsmi):
        if self.tvDurum == "Açık":
            if (kanalIsmi not in self.kanalListesi):
                self.kanalListesi.append(kanalIsmi)
        else:
            print("Kanal ekleme işlemi tv durumu kapalı olduğu için yapılamamaktadır.")
    def rastgeleKanal(self):
        if self.tvDurum == "Açık":
            rand = random.randint(0,len(self.kanalListesi)-1)
            self.kanal = self.kanalListesi[rand]
            print("Şu anki kanal : ",self.kanal)
        else:
            print("Rastgele kanala geçme işlemi tv durumu kapalı olduğu için yapılamamaktadır.")
    def menu(self):
        print("""
            Kumanda Uygulamasına Hoşgeldiniz
            1. Tv aç
            2. Tv kapat
            3. Ses ayarları
            4. Kanal ekle
            5. Kanal sayısı öğrenme
            6. Rastgele kanala geçme
            7. Televizyon bilgileri
            Çıkmak için 'q' yazın
            """)
    def __len__(self):
        return len(self.kanalListesi)
    def __str__(self):
        return "TvDurum : {}\nTvSes : {}\nKanalListesi : {}\nKanal : {}".format(self.tvDurum,self.tvSes,self.kanalListesi,self.kanal)
    
kumanda = Kumanda()

while True:
    kumanda.menu()
    islem = input("İşlemi Seçiniz : ")
    if(islem == "q"):
        print("Programdan çıkılıyor ..")
        break
    elif(islem == "1"):
        kumanda.tvAc()
    elif(islem == "2"):
        kumanda.tvKapat()
    elif(islem == "3"):
        kumanda.sesAyarlari()
    elif(islem == "4"):
        kanalTemp = input("Eklemek istediğiniz kanalların arasına , işareti koyarak yazınız")
        kanalListesi = kanalTemp.split(",")
        for kanal in kanalListesi:
            kumanda.kanalEkle(kanal)
    elif(islem == "5"):
        print("Listede : ",len(kumanda)," adet kanal bulunmaktadır.")
    elif(islem == "6"):
        kumanda.rastgeleKanal()
    elif(islem == "7"):
        print(kumanda)
    else:
        print("Geçersiz işlem")

        