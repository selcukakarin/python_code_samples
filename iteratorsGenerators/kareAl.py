class KareAl():
    def __init__(self,max):
        self.max=max
        self.sayi=1
    def __iter__(self):
        return self
    def __next__(self):
        if(self.sayi<=self.max):
            self.sayi+=1
            return self.sayi**2
        else:
            self.sayi=1
            raise StopIteration
            
kareAlDene=KareAl(5)
iterator=iter(kareAlDene)

for i in kareAlDene:
    print(i)

print(next(iterator))