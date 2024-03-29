class Dosya():

    def __init__(self):
        with open("metin.txt","r",encoding="utf-8") as file:
            icerik=file.read()
            kelimeler=icerik.split()
            self.sadeKelimeler=[]

            for i in kelimeler:
                i=i.strip("\n")
                i=i.strip(".")
                i=i.strip(",")
                self.sadeKelimeler.append(i)
            
            # for i in self.sadeKelimeler:
            #     print(i)

    def tumKelimeler(self):
        kelimelerKumesi=set()
        for i in self.sadeKelimeler:
            kelimelerKumesi.add(i)
        print("Tüm kelimeler ......")
        for i in kelimelerKumesi:
            print(i)
            print("******************")

    def kelimeFrekansi(self):
        kelimeSozluk=dict()
        for i in self.sadeKelimeler:
            if(i in kelimeSozluk):
                kelimeSozluk[i]+=1
            else:
                kelimeSozluk[i]=1
        for kelime,sayi in kelimeSozluk.items():
            print("{} kelimesi {} defa geçiyor.....".format(kelime,sayi))
            print("----------------------------")

dosya=Dosya()
dosya.tumKelimeler()
dosya.kelimeFrekansi()