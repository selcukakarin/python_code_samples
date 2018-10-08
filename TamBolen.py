def tamBolen(sayi):
    tamBolenler=[]

    for i in range(2,sayi):
        if(sayi%i==0):
            tamBolenler.append(i)
    return tamBolenler

while True:
    sayi=input("sayı gir")

    if(sayi=="q"):
        print("Programdan çıkılıyor")
        break
    else:
        sayi=int(sayi)
        print(tamBolen(sayi))