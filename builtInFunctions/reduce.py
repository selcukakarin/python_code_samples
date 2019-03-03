from functools import reduce
# def toplama(x,y):
#     return x+y
# print(reduce(toplama,[5,10,15,20]))

print(reduce(lambda x,y:x**y,[1,2,3,4]))

print(reduce(lambda x,y:x*y,[1,2,3,4]))

def maksimum(x,y):
    if(x>y):
        return x
    else:
        return y
print(reduce(maksimum,[-4,-20,30,55,2]))