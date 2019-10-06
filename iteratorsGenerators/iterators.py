# # iterator oluşturma
# liste=[1,14,3,4,5]
# # print(dir(liste))
# iterator=iter(liste)
# print(iterator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# # print(next(iterator))           #Stop iteration error

# liste=[1,3,5,8,9,190]
# for i in liste:
#     print(i)

#  ########## Yukarıdaki for döngüsünün yaptığı iş
# iterator=iter(liste)
# while True:
#     try:
#          print(next(iterator))
#     except StopIteration:
#         break

class Kumanda():
    def __init__(self,kanalListesi):
        self.kanalListesi=kanalListesi
        self.index=-1
    def __iter__(self):
        return self
    def __next__(self):
        self.index+=1
        if self.index < len(self.kanalListesi):
            return self.kanalListesi[self.index]
        else:
            self.index=-1
            raise StopIteration

kumanda=Kumanda(["Atv","trt","fox","kanal d"])
iterator=iter(kumanda)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))  #Stop iterations error

for i in kumanda:
    print(i)