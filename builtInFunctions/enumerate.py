liste=["Elma","Armut","Karpuz","Muz"]
i=0
sonuc=list()
while(i<len(liste)):
    sonuc.append((i,liste[i]))
    i+=1
print(sonuc)
print(list(enumerate(liste)))