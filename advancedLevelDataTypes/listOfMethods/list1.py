liste=[1,2,3,4,5]
liste.append(6)
print(liste)

liste1=[3,5,5,8,9,10]
liste2=["Selçuk","Deneme",1,55]
liste1.extend(liste2)       #extend bir listeyi diğer listeye ekler
print(liste1)

liste=[1,2,3,4,5]
liste.insert(3,"İstanbul")
print(liste)
liste.pop()
print(liste)
liste.pop(3)
print(liste)
liste.remove(3)
print(liste)

liste=[1,2,3,4,5,3,2,3,4,5]
print(liste.index(3))
print(liste.index(3,3))  # 3. indexten itibaren  3'ü ara
print(liste.count(3))
liste.sort()
print(liste)
liste.sort(reverse=True)
print(liste)