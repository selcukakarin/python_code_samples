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

