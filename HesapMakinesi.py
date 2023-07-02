print("""*************************
Hesap Makinesi Programı

İşlemler;

1. Toplama
2. Çıkarma
3. Çarpma
4. Bölme
*************************
""")

a=int(input("Birinci sayı : "))
b=int(input("ikinci sayı : "))

işlem=(int(input("işlemi giriniz")))

if işlem==1:
    print("{} ile {} toplamı {}'dir".format(a,b,a+b))
elif işlem==2:
    print("{} ile {} farkı {}'dir".format(a,b,a-b))
elif işlem==3:
    print("{} ile {} çarpımı {}'dir".format(a,b,a*b))
elif işlem==4:
    print("{} ile {} bölümü {}'dir".format(a,b,a/b))
else:
    print("Geçersiz işlem")
