print(list(filter(lambda x:x%2==0,[1,23,34,546,6576,2])))

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
print(list(filter(asalMi,range(1,100))))