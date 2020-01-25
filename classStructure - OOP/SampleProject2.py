import time
class Computer():
    def __init__(self,displayCard="GeForce GTX1660Ti ",processor="i7",ram=16,ssd=256,pcStatus="Closed"):
        self.displayCard=displayCard
        self.processor=processor
        self.ram=ram
        self.ssd=ssd
        self.pcStatus=pcStatus
    def __str__(self):
        return "DisplayCard : {}\Processor : {}\nRam : {}\nSsd : {}".format(self.displayCard,self.processor,self.ram,self.ssd,self.pcStatus)
    def __len__(self):
        return self.ram
    def showInfos(self):
        print("""
            Computer Infos
            Display Card : {}
            Processor : {}
            Ram : {}
            SSD : {}
            Pc Status : {}
        """.format(self.displayCard,self.processor,self.ram,self.ssd,self.pcStatus))
    def menu(self):
        print("""
            Welcome to Computer App
            1. Show infos
            2. Pc open
            3. Pc close
            4. Change a part
            q. Quit
        """)
    def openPc(self):
        if(self.pcStatus == "Opened"):
            print("Pc is already opened.")
        else:
            print("Pc opening.")
            time.sleep(1)
            print("Pc's opened.")
            self.pcStatus = "Opened"
            print("Pc status : {}".format(self.pcStatus))
    def closePc(self):
        if(self.pcStatus == "Closed"):
            print("Pc is already closed.")
        else:
            print("Pc is closing.")
            time.sleep(1)
            print("Pc's closed.")
            self.pcStatus = "Closed"
            print("Pc Status : {}".format(self.pcStatus))
    def changeAPart(self,part,newPart):
        if(part == "displayCard"):
            self.displayCard = newPart
        elif(part == "processor"):
            self.processor = newPart
        elif(part == "ram"):
            self.ram = newPart
        elif(part == "ssd"):
            self.ssd = newPart
        else:
            print("there is no such element")
    
computer = Computer(displayCard="‎MSI GeForce RTX2080 ",processor="i9",ram=64,ssd=512,pcStatus="Closed")
while True:
    computer.menu()
    choose = input("Chose an option")
    if(choose == "q"):
        print("The program is terminating")
        time.sleep(1)
        print("The program's terminated")
        break
    elif(choose == "1"):
        computer.showInfos()
    elif(choose == "2"):
        computer.openPc()
    elif(choose == "3"):
        computer.closePc()
    elif(choose == "4"):
        part = input("Enter the part to be replaced")
        newPart = input("Enter the new part")
        computer.changeAPart(part,newPart)

