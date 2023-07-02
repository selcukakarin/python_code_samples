def ekok(sayi1,sayi2):
    ekok=1
    k=0
    liste1=[2,3,5,7,11,13]
    liste2=[0,0,0,0,0,0]
    if(sayi1==sayi2):
        return sayi1
    else:
        for i in liste1:
            while sayi1%i==0 or sayi2%i== 0:
                if(sayi1%i==0):
                    sayi1//=i
                if(sayi2%i==0):
                    sayi2//=i
                liste2[k]+=1
            k+=1
    for i in range(0,len(liste1)):
        if(liste2[i]!=0):
            ekok*=liste1[i]**liste2[i]
    return ekok

x=int(input("sayı gir "))
y=int(input("sayı gir "))
print(ekok(x,y))
