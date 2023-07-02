def kareleriAl():
    sonuc=[]
    for i in range(1,6):
        sonuc.append(i**2)
    return sonuc

print(kareleriAl())

def kareleriAl():
    for i in range(1,6):
        yield i**2          ## yield sadece iterator ile çağırıldığı vakit bir değer üretir ############# Hafızada saklamaz
generator=kareleriAl()
print(generator)

iterator=iter(generator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))       # Stop iteration error

iterator2=iter(generator)   
print(next(iterator))           #Stop iteration error aldık çünkü generator daha önceden değerleri üretti ve tekrar değer 
                                #üretilmesi lazımsa tekrar generator üretmek gerekiyor


######## LİST COMPREHENSİON'ı generator'a çevirme
liste=[i*3 for i in range(5)]
print(liste)

#### herhangi bir değer üretilmedi sadece generator oluşturuldu
generator=(i*3 for i in range(5))
print(generator)

iterator=iter(generator)
print(next(iterator))
print(next(iterator))
print(next(iterator))

def carpimTablosu():
    for i in range(1,11):
        for j in range(1,11):
            yield "{} x {} = {}".format(i,j,i*j)
for i in carpimTablosu():
    print(i)