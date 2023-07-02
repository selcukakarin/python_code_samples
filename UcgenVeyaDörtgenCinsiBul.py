
choice=int(input("Üçgen mi bulmak istiyon kare mi? (üçgen=1,kare=2"))

if(choice==1):
    a=int(input("1. kenar "))
    b = int(input("2. kenar "))
    c = int(input("3. kenar "))
    if(a+b<c or a+c<b or b+c<a):
        print("böyle bir üçgen tanımlanamaz")
    else:
        if(a==b or a==c or b==c):
            print("ikiz kenar üçgen ")
        elif(a==b and a==c):
            print("eşkenar üçgen")
        else:
            print("sıradan üçgen")
elif(choice==2):
    a = int(input("1. kenar "))
    b = int(input("2. kenar "))
    c = int(input("3. kenar "))
    d=int(input("4. kenar "))
    if(a==b==c==d):
        print("karedir")
    elif((a==b and c==d)or(a==c or b==d)or(a==d or b==c)):
        print("dikdörtgendir")
    else:
        print("normal bir dörtgendir.")