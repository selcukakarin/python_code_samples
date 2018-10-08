a=int(input("a (x²'nin katsayısı):"))
b=int(input("b(x'in katsayısı):"))
c=int(input("c(sabitin katsayısı):"))

delta=a**2-4*a*c

x1=(-b-delta**0.5)/(2*a)

x2=(-b+delta**0.5)/(2*a)

print("Birinci kök : {}\nİkinci kök: {}\n".format(x1,x2))