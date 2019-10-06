def fonksiyon(*args):  # *arg ile gelen parametreler demetlere (tuple) dönüşür
    for i in args:
        print(i)
print(fonksiyon(1,2,3))
print(fonksiyon(1,2,3,4,5,6))

def fonksiyon2(isim,*args):
        print("İsim : ",isim)
        print("------------")
        for i in args:
                print(i)
fonksiyon2("Selçuk",1,2,3,4,5)

def fonksiyon3(**kwargs):
        print(kwargs)
fonksiyon3(isim="Selçuk",soyisim="Akarın",numara=11)

def fonksiyon4(**kwargs):               #kwargs göndeilen değerleri sözlük yapısı şekline çevirir
        for i,j in kwargs.items():
                print("Argüman ismi: ",i," Argüman değeri: ",j)
fonksiyon4(isim="Selçuk",soyisim="Akarın",numara=11)

def fonksiyon5(*args,**kwargs):
        for i in args:
                print(i)
        print("-----------")
        for i,j in kwargs.items():
                print(i,j)
fonksiyon5(1,2,3,4,5,6,isim="Selçuk",soyisim="Akarın",numara=11)