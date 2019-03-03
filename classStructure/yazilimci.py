class Yazilimci():
    def __init__(self,isim,soyisim,numara,maas,diller):
        self.isim=isim
        self.soyisim=soyisim
        self.numara=numara
        self.maas=maas
        self.diller=diller
    def bilgileriGoster(self):
        print("""
        Yazılımcı objesinin özellikleri

        İsim : {}

        Soyisim : {}

        Numara : {}

        Maaş : {}

        Bilgidiği diller : {}
        
        """.format(self.isim,self.soyisim,self.numara,self.maas,self.diller))

    def zamYap(self,zamMiktari):
        print("Zam yapılıyor...")
        self.maas+=zamMiktari

    def dilEkle(self,dil):
        print("Dil ekleniyor..")
        self.diller.append(dil)

yazilimci=Yazilimci("Selçuk","Akarın",1234,3000,["Python","Java","C#"])
print(yazilimci.bilgileriGoster())

yazilimci.dilEkle("C++")
print(yazilimci.bilgileriGoster())

yazilimci.zamYap(1100)
print(yazilimci.bilgileriGoster())