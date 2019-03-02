def asalMi(x):
    i=2
    if(x==1):
        return False
    elif(x==2):
        return True
    else:
        while(i<x):
            if(x%i==0):
                return False
            i+=1
        return True

print(asalMi(1))
print(asalMi(2))
print(asalMi(17))
print(asalMi(100))

print(list(filter(asalMi,range(1,100))))