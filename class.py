class Yazılımcı:
    def __init__(self,isim,soyisim,numara,maas,diller):
        self.isim=isim
        self.soyisim=soyisim
        self.numara=numara
        self.maas=maas
        self.diller=diller
    def bilgileriGoster(self):
        print("""
        
        Yazılımcı objesinin özellikleri

        İsim: {}

        Soyisim: {}

        Numara: {}

        Maaş: {}

        Bildiği Diller: {}

        """.format(self.isim,self.soyisim,self.numara,self.maas,self.diller))
    def zamYap(self,zamMiktarı):
        print("Zam Yapılıyor...")

        self.maas+=zamMiktarı
    def dilEkle(self,yeniDil):
        print("Dil ekleniyor...")
        self.diller.append(yeniDil)


yazılımcı= Yazılımcı("Selçuk","Akarın",10,3000,["Python","Java","C"])
yazılımcı.bilgileriGoster()

yazılımcı.dilEkle("GoLang")
yazılımcı.bilgileriGoster()

yazılımcı.zamYap(500)
yazılımcı.bilgileriGoster()
