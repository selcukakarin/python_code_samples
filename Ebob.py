def ebob(sayi1,sayi2):
    ebob=1;
    if(sayi1==sayi2):
        return sayi1
    else:
        if(sayi1>sayi2):
            for i in range(1,sayi2+1):
                if(sayi1%i==0 and sayi2%i==0):
                    ebob=i
        else:
            for i in range(1, sayi1+1):
                if (sayi1 % i == 0 and sayi2 % i == 0):
                    ebob = i
    return ebob

x=int(input("sayı gir "))
y=int(input("sayı gir "))
print(ebob(x,y))