liste1=list()
for i in range(1,10):
    liste1.append(i)
liste2=[i for i in liste1 if(i%2==0)]
print(liste2)