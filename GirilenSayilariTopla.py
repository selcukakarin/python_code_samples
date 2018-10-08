toplam=0
print("çıkış için q'ya basın")
while True:
    sayi=input("sayı gir : ")
    if(sayi=="q"):
       break
    toplam+=int(sayi)
print("toplam {}".format(toplam))