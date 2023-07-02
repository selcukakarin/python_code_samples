import random
import time

print("""**********************************

Sayi Tahmin Oyunu

1 ile 40 arasında sayı tahmin et

**********************************
""")

rastgeleSayi=random.randint(1,40)
tahminHakki=7
while True:
    tahmin=int(input("Tahmininiz: "))

    if(tahmin<rastgeleSayi):
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Daha yüksek bir sayı söyleyin...")
        tahminHakki-=1
    elif(tahmin>rastgeleSayi):
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Daha düşük bir sayı söyleyin...")
        tahminHakki-=1
    else:
        print("Bilgiler sorgulanıyor")
        time.sleep(1)
        print("Tebikler doğru yanıt : ",rastgeleSayi)
        break