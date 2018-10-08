def mukemmelSayiBul(sayi):
    toplam=0
    for i in range(1,int(sayi/2)+1):
        if(sayi%i==0):
            toplam+=i
    if (toplam==sayi):
        return True
    return False

for i in range(1,1000):
    if(mukemmelSayiBul(i)):
        print(i)