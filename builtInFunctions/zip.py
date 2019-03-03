liste1=[1,2,3,4,5]
liste2=[6,7,8,9,10,11]
liste3=["Python","Php","Java","C#"]
# i=0
# sonuc=list()
# while(i<len(liste1) and i<len(liste2)):
#     sonuc.append((liste1[i],liste2[i]))
#     i+=1
# print(sonuc)
# print(list(zip(liste1,liste2, liste3)))

for i,j,k in zip(liste1,liste2,liste3):
    print(i,j,k)

sozluk1={"Elma":1,"Armut":2,"Kiraz":3}
sozluk2={"Sıfır":0,"Bir":1,"iki":2}
print(list(zip(sozluk1,sozluk2)))
print(list(zip(sozluk1.values(),sozluk2.values())))