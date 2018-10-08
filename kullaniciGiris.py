print("""
***********************
Kullanıcı Girişi Programı
***********************
""")

sysKullaniciAdi="Selçuk"

sysParola="12345"

girisHakki=3

while True:
    kullanicAdi=input("Kullanıcı Adı : ")
    parola=input("Parola :  ")
    if(kullanicAdi!=sysKullaniciAdi and parola==sysParola):
        print("Kullanıcı adı yanlış")
        girisHakki-=1
    elif(kullanicAdi==sysKullaniciAdi and parola!=sysParola):
        print("Parola yanlış")
        girisHakki-=1
    elif (kullanicAdi != sysKullaniciAdi and parola != sysParola):
        print("Kullanıcı adı ve Parola yanlış")
        girisHakki -= 1
    else:
        print("sisteme hg")
        break
    if(girisHakki==0):
        print("giriş hakkınızı bitti")
        break