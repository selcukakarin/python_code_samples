class Kitap():
    def __init__(self,isim,yazar,sayfaSayisi,tur):
        print("init fonksiyonu")
        self.isim=isim
        self.yazar=yazar
        self.sayfaSayisi=sayfaSayisi
        self.tur=tur
    def __str__(self):
        return "İsim: {}\nYazar: {}\nSayfa sayısı: {}\nTürü: {}".format(self.isim,self.yazar,self.sayfaSayisi,self.tur)
    def __len__(self):
        return self.sayfaSayisi
    def __del__(self):
        print("Kitap objesi siliniyor..")

kitap=Kitap("Dönüşüm","Franz Kafka",70,"Hikaye")

print(kitap)
print(len(kitap))
del kitap