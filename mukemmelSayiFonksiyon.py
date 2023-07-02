def mukemmelBul(sayi):
    toplam=0
    for i in range(1,sayi):
        if(sayi%i==0):
            toplam+=i
    if(toplam==sayi):
        return True
    else:
        return False

for i in range(1,1001):
    if(mukemmelBul(i)):
        print(i," mükemmel sayıdır.")
