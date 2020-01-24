class Yazılımcı():
    
    def __init__(self,isim,soyisim,numara,maaş,diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara    # Yazılımcı objelerinin özellikleri 
        self.maaş = maaş
        self.diller = diller

# yazılımcı1 objesi
yazılımcı1 =  Yazılımcı("Furkan","Sarikaya",3322,4000,["C#","C","Java"])

yazılımcı2 = Yazılımcı("Selçuk","Akarın",23456,3500,["C","R","Java"])

print(yazılımcı1.diller)

print(yazılımcı2.soyisim)

class Yazılımcı():
    
    def __init__(self,isim,soyisim,numara,maaş,diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara    # Yazılımcı objelerinin özellikleri 
        self.maaş = maaş
        self.diller = diller
    def bilgilerigöster(self):
        print("""
        Çalışan Bilgisi:
        
        İsim :  {}
        
        Soyisim : {}
        
        Şirket Numarası: {}
        
        Maaş :  {}
        
        Diller: {}
        """.format(self.isim,self.soyisim,self.numara,self.maaş,self.diller))

yazılımcı1 =  Yazılımcı("Mustafa","Akarın",12345,3000,["Python","C","Java"])  
yazılımcı1.bilgilerigöster()


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