try:
    a=int("asdasd123")
    print("program burada")
except :
    print("Bir hata oluştu")
print("Bloklar sonlandı.")

try:
    a=int("asdasd123")
    print("program burada")
except ValueError:
    print("Bir valueError hatası oluştu")
print("Bloklar sonlandı.")

try:
    a=int(input("Sayı 1 : "))
    b=int(input("Sayı 2 : "))
    print(a/b)
except ValueError:
    print("Lütfen string girmeyin")
except ZeroDivisionError:
    print("0'a bölme hatası oldu")

try:
    a=int(input("Sayı 1 : "))
    b=int(input("Sayı 2 : "))
    print(a/b)
except (ValueError,ZeroDivisionError):
    print("ValuError veya ZeroDivision")

try:
    a=int(input("Sayı 1 : "))
    b=int(input("Sayı 2 : "))
    print(a/b)
except ValueError:
    print("Lütfen string girmeyin")
except ZeroDivisionError:
    print("0'a bölme hatası oldu")
finally:
    print("Finally çalıştı")

def tersCevir(s):
    if(type(s)!=str):
        raise ValueError("Lütfen string giriniz. ")
    else:
        return s[::-1]
print(tersCevir("Selçuk"))

try:
    print(tersCevir(11))
except ValueError:
    print("Foksiyon hata verdi.")