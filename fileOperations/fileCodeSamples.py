file=open("bilgiler.txt","w")
file.close()

file=open("C:/Users/selcuk/Desktop/bilgiler.txt","w",encoding="utf-8")
file.write("Selçuk akarın")
file.close()

file=open("bilgiler.txt","a",encoding="utf-8")
file.write("Selçuk Akarın")
file.close()

file=open("bilgiler.txt","r")
file.close()

try:
    file=open("bilgiler2.txt","r")
except FileNotFoundError:
    print("Dosya bulunamadı..")

file=open("bilgiler.txt","r",encoding="utf-8")
for i in file:
    print(i,end="")
file.close()

file=open("bilgiler.txt","r",encoding="utf-8")
icerik=file.read()
print("Dosyanın içeriği : {}".format(icerik))

file=open("bilgiler.txt","r",encoding="utf-8")
print(file.readline())
file.close()

file=open("bilgiler.txt","r",encoding="utf-8")
print(file.readlines())
file.close()