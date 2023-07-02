with open("bilgiler.txt","r",encoding="utf-8")as file:   ##safety usage
    for i in file:
        print(i)

with open("bilgiler.txt","r",encoding="utf-8")as file:
    print(file.tell())    # imlecin bulunduğu index
    file.seek(15)         # imlecin bulunacağı indexi belirler
    print(file.tell())


with open("bilgiler.txt","r",encoding="utf-8")as file:
    file.seek(5)
    icerik=file.read(12)
    print(icerik)

with open("bilgiler.txt","r",encoding="utf-8")as file:
    print(file.tell())
    file.seek(15)
    print(file.tell())
    file.seek(0)
    icerik=file.read(6)
    print(icerik)

with open("bilgiler.txt","r+",encoding="utf-8")as file:   # r+ hem dosya okur hem yazar
    file.seek(10)
    file.write("DENEME")
    file.seek(0)
    print(file.read())

# Dosyanın sonuna string ekleme
with open("bilgiler.txt","a",encoding="utf-8")as file:
    file.write("Abdülsamed Yıldırım\n")
with open("bilgiler.txt","r+",encoding="utf-8")as file:
    print(file.read())

# Dosyanın başına string ekleme
with open("bilgiler.txt","r+",encoding="utf-8")as file:
    icerik=file.read()
    icerik="Furkan Sarıkaya\n"+icerik
    file.seek(0)
    file.write(icerik)
    file.seek(0)
    print(file.read())

with open("bilgiler.txt","r+",encoding="utf-8") as file:
    liste=file.readlines()
    liste.insert(3,"DENEME DENEME\n")
    print(liste)
    file.seek(0)
    for i in liste:
        file.write(i)
    file.writelines(liste)
    file.seek(0)
    print(file.read())