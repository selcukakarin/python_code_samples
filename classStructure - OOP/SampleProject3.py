import time
class Animal():
    def __init__(self,name="Boncuk",color="White",age=2,isHungry=True,isTired=False):
        print("Animal has created")
        self.name = name
        self.color = color
        self.age = age
        self.isHungry = isHungry
        self.isTired = isTired
    def showInfos(self):
        print("""
            Showing Animal Infos
            Name : {}
            Color : {}
            Age : {}
            isHungry : {}
            isTired : {}\n
        """.format(self.name,self.color,self.age,self.isHungry,self.isTired))
    def menu(self):
        print("""
            Showing Menu
            1. ShowInfos
            2. Make a sound
            3. move
            4. stop
            5. eat
            6. rest
            q. Quit\n
        """)
    def makeASound(self):
        print("Animal is making sound...")
    def move(self):
        print("Animal is moving...")
        self.isTired = True
        self.isHungry = True
    def stop(self):
        print("Animal has stopped.")
    def eat(self):
        print("Animal is eating...")
        isHungry = False
    def rest(self):
        print("Animal is resting...")
        isTired = False

class Cat(Animal):
    def __init__(self,name="Boncuk",color="White",age=2,isHungry=True,isTired=False,isNeedShave=False):
        print("Cat has created")
        super().__init__(name,color,age,isHungry,isTired)
        self.isNeedShave = isNeedShave
    def makeASound(self):
        print("Cat is meowing...")
    def scratch(self):
        print("Cat is scratching")
class Dog(Animal):
    def __init__(self,name="Mike",color="White",age=2,isHungry=True,isTired=False,isNeedLeash=False):
        print("Dog has created")
        super().__init__(name,color,age,isHungry,isTired)
        self.isNeedLeash = isNeedLeash
    def makeASound(self):
        print("Dog is barking...")
    def bite(self):
        print("Dog is biting")
class Horse(Animal):
    def __init__(self,name="Grace's Secret",color="White",age=2,isHungry=True,isTired=False,isNeedHorseShoe=False):
        print("Horse has created")
        super().__init__(name,color,age,isHungry,isTired)
        self.isNeedHorseShoe = isNeedHorseShoe
    def makeASound(self):
        print("Horse is neighing")
    def kick(self):
        print("Horse is kicking someone")

animalList = list()

while True:
    print("""
        Welcome to ZooaaP
        Options
        animal
        cat
        dog
        horse
        q = Quit\n
    """)
    choose = input("Make a choose\n")
    if(choose == "q"):
        print("Program is terminated\n")
        time.sleep(1)
        print("Program terminated\n")
        break
    name = input("name : ")
    color = input("color : ")
    age = input("age : ")
    isHungry = input("isHungry : ")
    isTired = input("isTired : ")
    if(choose == "animal"):
        animal = Animal(name=name,color=color,age=age,isHungry=isHungry,isTired=isTired)
        animalList.append(animal)
    elif(choose == "cat"):
        isNeedShave = input("isNeedShave : ")
        cat = Cat(name=name,color=color,age=age,isHungry=isHungry,isTired=isTired,isNeedShave=isNeedShave)
        animalList.append(cat)
    elif(choose == "dog"):
        isNeedLeash = input("isNeedLeash : ")
        dog = Dog(name=name,color=color,age=age,isHungry=isHungry,isTired=isTired,isNeedLeash=isNeedLeash)
        animalList.append(dog)
    elif(choose == "horse"):
        isNeedHorseShoe = input("isNeedHorseShoe : ")
        horse = Horse(name=name,color=color,age=age,isHungry=isHungry,isTired=isTired,isNeedHorseShoe=isNeedHorseShoe)
        animalList.append(horse)
while True:
    change = input("Would you like change the animal? Yes = y, No = n")
    if(change == "y"):
        for index in range(len(animalList)):
            print("{}. Age : {} - Name : {}".format(index,animalList[index].age,animalList[index].name))
        chosenIndex = input("Choose an animal to make process (0,1,..)\n")
    print("Choosen animal {}\n".format(animalList[chosenIndex]))
    animalList[chosenIndex].menu()
    selected = input("Choose an option")
    if(option == "q"):
        print("Program is terminating")
        time.sleep(1)
        print("Program has terminated")
    elif(option == "1"):
        animalList[chosenIndex].makeASound()
    elif(option == "2"):
        animalList[chosenIndex].move()
    elif(option == "3"):
        animalList[chosenIndex].stop()
    elif(option == "4"):
        animalList[chosenIndex].eat()
    elif(option == "5"):
        animalList[chosenIndex].rest()


    
    