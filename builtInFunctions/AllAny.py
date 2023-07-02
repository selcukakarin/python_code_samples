def hepsi(liste):
    for i in liste:
        if not i:
            return False
    return True
liste=[True,False,True,False,True]
print(hepsi(liste))

liste=[1,2,3,4,5]
print(hepsi(liste))

def herhangi(liste):
    for i in liste:
        if i:
            return True
    return False
    
print(herhangi([True,False,True,False,True]))

liste2=[0,0,0,0,0,0]
print(herhangi(liste2))

liste=[1,2,3,4,5]
print(all(liste))

liste2=[0,0,0,0,0,0]
print(any(liste2))
