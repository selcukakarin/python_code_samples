def selamla(isim):
    print("merhaba",isim)
selamla("selçuk")

merhaba=selamla         #fonksiyonların değişken olarak tanımlanması

print(selamla)
print(merhaba)

merhaba("Alican")

del selamla

print(merhaba)
print(selamla)

#########

def fonksiyon():
    def fonksiyon2():
        print("küçük fonksiyondan herkese selamlar")
    fonksiyon2()
    print("Büyük fonksiyondan herkese merhaba")
fonksiyon()

def fonksiyon(*args):
    def toplama(args):
        toplam=0
        for i in args:
            toplam+=i
        return toplam
    print(toplama(args))
fonksiyon(1,2,3,4,5,6,7)

def anaFonksiyon(islemAdi):
    def toplama(*args):
        toplam=0
        for i in args:
            toplam+=i
        return toplam
    def carpim(*args):
        carpim=1
        for i in args:
            carpim*=i
        return carpim
    if islemAdi=="toplama":     #fonksiyon içinden return ile fonksiyon gönderdik
        return toplama
    else:
        return carpim
        
fonk=anaFonksiyon("toplama")
print(fonk(1,2,3,4,5,6))

fonk2=anaFonksiyon("carpim")
print(fonk2(1,2,3,4,5))


## Bir fonksiyona argüman olarak fonksiyon gönderme
def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b

def anaFoksiyon(func1,func2,func3,func4,islemAdi):
    if islemAdi=="toplama":
        print(func1(3,4))
    elif islemAdi=="çıkarma":
        print(func2(3,4))
    elif islemAdi=="çarpma":
        print(func3(3,4))
    elif islemAdi=="bölme":
        print(func4(3,4))
    else:
        print("Geçersiz işlem")
anaFoksiyon(toplama,cikarma,carpma,bolme,"toplama")    
anaFoksiyon(toplama,cikarma,carpma,bolme,"çıkarma")    
anaFoksiyon(toplama,cikarma,carpma,bolme,"çarpma")    
anaFoksiyon(toplama,cikarma,carpma,bolme,"bölme")    
