""" with open("bilgiler.txt","r+",encoding="utf-8") as file:
    icerik=file.read()
    icerik="Deneme Deneme\n"+icerik
    file.seek(0)
    file.write(icerik) """

with open("bilgiler.txt","r+",encoding="utf-8") as file:
    print(file.read())