import time

def zamanHesapla(func):
    def wrapper(sayilar):
        baslama=time.time()

        sonuc=func(sayilar)

        bitis=time.time()

        print(func.__name__+" "+str(bitis-baslama)+" saniye sürdü.")
        return sonuc
    return wrapper

@zamanHesapla       # zamanHesapla decorator'ımızı kareleriHesapla fonksiyonumuza ekledik
def kareleriHesapla(sayilar):
    sonuc=list()
    # baslama=time.time()         # for baslamadan önce programın harcadığı zaman
    for i in sayilar:
        sonuc.append(i**2),
    # bitis=time.time()       # for'dan sonra programın harcadığı zaman
    # print("Bu fonksiyon "+str(bitis-baslama)+" saniye sürdü.")
    return sonuc

@zamanHesapla
def kupleriHesapla(sayilar):
    sonuc=list()
    # baslama=time.time()
    for i in sayilar:
        sonuc.append(i**3)
    # bitis=time.time()
    # print("Bu fonksiyon "+str(bitis-baslama)+" saniye sürdü.")
    return sonuc
kareleriHesapla(range(100000))
kupleriHesapla(range(100000))
