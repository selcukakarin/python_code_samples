def tamBolenleriBul(sayi):
    tamBolenler=[]
    for i in range(1,sayi+1):
        if(sayi%i==0):
            tamBolenler.append(i)
    return tamBolenler

while True:
    sayi=input("Sayi : ")
    if(sayi=="q"):
        print("programdan çıkılıyor...")
        break
    else:
        sayi=int(sayi)
        print("Tam Bolenler = ",tamBolenleriBul(sayi))