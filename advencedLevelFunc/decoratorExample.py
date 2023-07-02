def ekstra(fonk):
    def wrapper(sayilar):
        ciftlerToplami=0
        ciftSayilar=0
        teklerToplami=0
        tekSayilar=0
        for sayi in sayilar:
            if (sayi % 2 == 0):
                ciftlerToplami+=sayi
                ciftSayilar+=1
            else:
                teklerToplami+=sayi
                tekSayilar+=1
        print("Teklerin ortalaması : ",teklerToplami/tekSayilar)
        print("Çiftlerin ortalaması : ",ciftlerToplami/ciftSayilar)
        fonk(sayilar)
    return wrapper

@ekstra
def ortalamaBul(sayilar):
    toplam=0
    for sayi in sayilar:
        toplam+=sayi
    print("Genel ortalama : ",toplam/len(sayilar))
ortalamaBul([1,2,3,4,52,34,566,21])
