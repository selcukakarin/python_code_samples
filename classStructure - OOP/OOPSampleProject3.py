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
    def menu(self):
        print("""
            Showing Menu
            1. ShowInfos
            2. Make a sound
            3. move
            4. stop
            5. eat
            6. rest
            7. scratch
            q. Quit\n
        """)

class Dog(Animal):
    def __init__(self,name="Mike",color="White",age=2,isHungry=True,isTired=False,isNeedLeash=False):
        print("Dog has created")
        super().__init__(name,color,age,isHungry,isTired)
        self.isNeedLeash = isNeedLeash
    def makeASound(self):
        print("Dog is barking...")
    def bite(self):
        print("Dog is biting")
    def menu(self):
        print("""
            Showing Menu
            1. ShowInfos
            2. Make a sound
            3. move
            4. stop
            5. eat
            6. rest
            8. bite
            q. Quit\n
        """)

class Horse(Animal):
    def __init__(self,name="Grace's Secret",color="White",age=2,isHungry=True,isTired=False,isNeedHorseShoe=False):
        print("Horse has created")
        super().__init__(name,color,age,isHungry,isTired)
        self.isNeedHorseShoe = isNeedHorseShoe
    def makeASound(self):
        print("Horse is neighing")
    def kick(self):
        print("Horse is kicking someone")
    def menu(self):
        print("""
            Showing Menu
            1. ShowInfos
            2. Make a sound
            3. move
            4. stop
            5. eat
            6. rest
            9. kick
            q. Quit\n
        """)

animalList = list()

while True:
    print("""
        Welcome to ZooaaP
        Options
        - animal
        - cat
        - dog
        - horse
        - q = Quit\n
    """)
    choose = input("Make a choose\n")
    if(choose == "q"):
        print("Craeting is terminated\n")
        time.sleep(1)
        print("Craeting terminated\n")
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
for index in range(len(animalList)):
    print("{}. Age : {} - Name : {}".format(index,animalList[index].age,animalList[index].name))
chosenIndex = int(input("Choose an animal to make process (0,1,..)\n"))
while True:
    change = input("Would you like to change the animal? Yes = y, No = n\n")
    if(change == "y"):
        for index in range(len(animalList)):
            print("{}. Age : {} - Name : {}".format(index,animalList[index].age,animalList[index].name))
        chosenIndex = int(input("Choose an animal to make process (0,1,..)\n"))
    print("Choosen animal {}\n".format(animalList[chosenIndex].name))
    animalList[chosenIndex].menu()
    option = input("Choose an option\n")
    if(option == "q"):
        print("Program is terminating\n")
        time.sleep(1)
        print("Program has terminated\n")
        break
    elif(option == "1"):
        animalList[chosenIndex].showInfos()
    elif(option == "2"):
        animalList[chosenIndex].makeASound()
    elif(option == "3"):
        animalList[chosenIndex].move()
    elif(option == "4"):
        animalList[chosenIndex].stop()
    elif(option == "5"):
        animalList[chosenIndex].eat()
    elif(option == "6"):
        animalList[chosenIndex].rest()
    elif(option == "7"):
        animalList[chosenIndex].scratch()
    elif(option == "8"):
        animalList[chosenIndex].bite()
    elif(option == "9"):
        animalList[chosenIndex].kick()


    
    