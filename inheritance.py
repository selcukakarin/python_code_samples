class Calisan:
    def __init__(self,isim,maas,departman):
        print("calisan sinifinin init fonksiyonu")
        self.isim=isim
        self.maas=maas
        self.departman=departman
    def bilgileriGoster(self):
        print("calisan sinifinin bilgileri")
        print("İsim: {}\nMaas: {}\nDepartman: {}".format(self.isim,self.maas,self.departman))
    def departmaniDegistir(self,yeniDepartman):
        self.departman=yeniDepartman

class Yonetici(Calisan):
    def __init__(self,isim,maas,departman,kisiSayisi=3):
        super().__init__(isim,maas,departman)
        print("Yonetici fonksiyonunun init fonksiyonu")

        self.kisiSayisi=kisiSayisi
    def zamYap(self,zamMiktari):
        self.maas+=zamMiktari
    def bilgileriGoster(self):
        print("Yonetici sinifinin bilgileri")
        print("İsim: {}\nMaas: {}\nDepartman: {}\nKisi: {}".format(self.isim,self.maas,self.departman,self.kisiSayisi))

yonetici=Yonetici("Selçuk",5000,"Bilişim")
yonetici.bilgileriGoster()

yonetici.zamYap(350)
yonetici.bilgileriGoster()