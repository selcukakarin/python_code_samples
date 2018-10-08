sayi=input("sayı gir : ")
toplam=0
basamak=len(sayi)
sayi=int(sayi)
tempsayi=sayi

while(tempsayi>0):
    toplam+=((tempsayi%10)**basamak)
    tempsayi//=10
if(toplam==sayi):
    print("bu sayı armstrong")
else:
    print("bu sayı armstrong değil")