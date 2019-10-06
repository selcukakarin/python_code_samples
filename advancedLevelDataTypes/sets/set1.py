x={1,2,3}
print(type(x))

liste=[1,1,1,1,2,2,2,3,3,3,3]
print(set(liste))

x={"Selçuk","Ali","Mahmut","Raşit","Selçuk"}
for i in x:
    print(i)
print("-------")
x.add("Selçuk")
for i in x:
    print(i)

# kume1={1,2,2,3,4,5,6}
# kume2={7,8,8,9,2,5,0,3,21,1}
# print(kume1.difference(kume2))
# print(kume1.difference_update(kume2))
# print(kume1)

# kume1={1,2,2,3,4,5,6}
# kume2={7,8,8,9,2,5,0,3,21,1}
# kume1.discard(2)      #kümeden eleman çıkart
# print(kume1)

kume1={1,2,2,3,4,5,6}
kume2={7,8,8,9,2,5,0,3,21,1}
print(kume1.intersection(kume2))   # intersection_update

kume1={1,2,2,3,4,5,6}
kume2={7,8,8,9,2,5,0,3,21,1}
kume3={-1,-2,-3}
print(kume1.isdisjoint(kume2))       #ayrık küme mi?
print(kume1.isdisjoint(kume3))

x={1,2,3}
y={1,2}
z={1,2,3,4,5}

print(x.issubset(y))        #alt kümesi mi?
print(y.issubset(x))
print(x.issubset(z))

kume1={1,2,2,3,4,5,6}
kume2={7,8,8,9,2,5,0,3,21,1}
print(kume1.union(kume2))
kume1.update(kume2)
print(kume1)