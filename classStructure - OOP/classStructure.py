#  Yeni bir Araba veri tipi oluşturuyoruz.
class Araba():
    model =  "Renault Megane"
    renk = "Gümüş"            # Sınıfımızın özellikleri (attributes)
    beygir_gücü = 110
    silindir = 4
    
araba1 =  Araba() # Araba veri tipinden bir "araba1" isminde bir obje oluşturduk.
print(araba1) # Objemizin veri tipi Araba
print(type(araba1))
print(araba1.model)
print(araba1.renk)
print(araba1.beygir_gücü)
print(araba1.silindir)

araba2 =  Araba()
print(araba2.model)
print(araba2.renk)
print(araba2.beygir_gücü)
print(araba2.silindir)

print(dir(araba1))

# Araba Veri tipi 

class Araba():
    # Şimdilik Class özelliklerine ihtiyacımız yok.
    
    def __init__(self):
        print("init fonksiyonu çağrıldı.")

araba1 = Araba() # araba1 objesi oluşurken otomatik olarak __init__ metodumuz çağrılıyor.

class Araba():
    
    def __init__(self,model,renk,beygir_gücü,silindir): # Parametrelerimizin değerlerini objelerimizi oluştururken göndereceğiz.
        self.model =  model # self.özellik_ismi = parametre değeri şeklinde objemizin model özelliğine değeri atıyoruz.
        self.renk = renk # self.özellik_ismi = parametre değeri şeklinde objemizin renk özelliğine değeri atıyoruz.
        self.beygir_gücü = beygir_gücü # self.özellik_ismi = parametre değeri şeklinde objemizin beygir_gücü özelliğine değeri atıyoruz.
        self.silindir = silindir # self.özellik_ismi = parametre değeri şeklinde objemizin silndir özelliğine değeri atıyoruz.

# araba1 objesini oluşturalım.
# Artık değerlerimizi göndererek objelerimizin özelliklerini istediğimiz değerle başlatabiliriz.
araba1 = Araba("Peugeot 301","Beyaz",90,4) 
print(araba1.model)
print(araba1.renk)
print(araba1.beygir_gücü)
print(araba1.silindir)

# araba2 objesini oluşturalım.
araba2 = Araba("Renault Megane","Gümüş",110,4)
print(araba2.model)
print(araba2.renk)
print(araba2.beygir_gücü)
print(araba2.silindir)

class Araba():

    def __init__(self,model="Bilgi yok",renk="Bilgi yok",beygir_gucu=70,silindir=4):
        print("init fonksiyonu çağrıldı.")

        self.model=model
        self.renk=renk
        self.beygir_gucu=beygir_gucu
        self.silindir=silindir

araba1=Araba(silindir=5)

print(araba1.renk)

#print(dir(Araba))  #dir ile classın tüm özelliklerini görebiliriz.

