def asalMi(sayi):
    if(sayi==1):
        return False
    elif(sayi==2):
        return True
    else:
        for i in range(2,sayi):
            if(sayi%i==0):
                return False
        return  True

while True:
    sayi =input("Sayı : ")
    if(sayi=="q"):
        break
    else:
        sayi=int(sayi)
        if(asalMi(sayi)):
            print(sayi," asal sayıdır")
        else:
            print(sayi," asal değil")