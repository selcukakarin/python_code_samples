import time
def islem():
    print("""
    ***********************
    Atm Makinesine Hoşgeldiniz
    ***********************
    İşlemler : 
    1. Bakiye Sorgula
    2. Para Yatır
    3. Para Çek
    Programdan çıkmak için q'ya basın
    ***********************
    """)


bakiye=1000
while True:
    islem()
    işlem=input("işlemi seçin : ")
    if(işlem=="q"):
        print("yine bekleriz")
        break
    elif(işlem=="1"):
        print("Bakiyeniz {} tldir".format(bakiye))
        time.sleep(3)
    elif (işlem == "2"):
        miktar=int(input("miktarı giriniz : "))
        bakiye+=miktar
        print("Bakiyeniz {} tldir".format(bakiye))
        time.sleep(3)
    elif(işlem=="3"):
        miktar=int(input("Miktarı giriniz : "))
        if(bakiye-miktar<0):
            print("Bakiyeniz yetersiz")
            continue
        bakiye-=miktar
        print("Bakiyeniz {} tldir".format(bakiye))
        time.sleep(3)

