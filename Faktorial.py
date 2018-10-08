print("""
**************************************
Faktoriyel bulma programına hoşgeldiniz

Çıkmak için q'ya basın
**************************************
""")

while True:
    sayi=input("Sayı : ")
    if(sayi=="q"):
        print("program sonlandırılıyor")
        break
    else:
        sayi=int(sayi)
        faktoriyel=1
        for i in range(2,sayi+1):
            faktoriyel*=i
        print("Faktöriyel : ",faktoriyel)