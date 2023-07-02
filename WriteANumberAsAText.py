def yaziIle(sayi):
    sozlukBirlik={1:" Bir",2:" İki",3:" Üç",4:" Dört",5:" Beş",6:" Altı",7:" Yedi",8:" Sekiz",9:" Dokuz"}
    sozlukİkilik={1:"On",2:"Yirmi",3:"Otuz",4:"Kırk",5:"Elli",6:"Altmış",7:"Yetmiş",8:"Seksen",9:"Doksan"}
    liste=[]
    control=0
    gecici=sayi

    while gecici>0:
        liste.append(gecici%10)
        gecici//=10
        control+=1
        if(control==2):
            break
    if(control==2):
        print(sozlukİkilik[liste[1]],sozlukBirlik[liste[0]])
    else:
        print("iki basamaklı sayı giriniz")

x=int(input("iki basamaklı sayı gir"))
yaziIle(x)