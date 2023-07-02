def calculateThePoints(fileLine):
    fileLine=fileLine[:-1]
    myList=fileLine.split(",")
    name=myList[0]
    point1=int(myList[1])
    point2=int(myList[2])
    point3=int(myList[3])
    lastPoint=point1*(3/10)+point2*(3/10)+point3*(4/10)
    if(lastPoint>=90):
        grade="A+"
    elif(lastPoint>=85):
        grade="A-"
    elif(lastPoint>=80):
        grade="B+"
    elif(lastPoint>=75):
        grade="B-"
    elif(lastPoint>=70):
        grade="C+"
    elif(lastPoint>=60):
        grade="C-"
    else:
        grade="F-"
    
    return name+" ------------> "+grade+"\n"


with open("dosya.txt","r",encoding="utf-8")as file:
    studentList=[]
    for i in file:
        studentList.append(calculateThePoints(i))
    
    with open("grades.txt","w",encoding="utf-8")as file2:
        for i in studentList:
            file2.write(i)