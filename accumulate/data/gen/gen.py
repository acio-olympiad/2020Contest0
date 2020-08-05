import random
Cases = []
def addcase(n,k,subtask):
    Cases.append([n,k,subtask])
    
def SB1():
    for i in range(15):
        addcase(10**5 - random.randint(0,10),1,1)
    addcase(2,1,1)
    addcase(3,1,1)

def SB2():
    for i in range(15):
        addcase(10**5,random.randint(1, 10**5-1), 2)
    addcase(2,1,2)
    addcase(3,1,2)
    addcase(3,2,2)

def SB3():
    for i in range(15):
        addcase(1000,random.randint(1, 999), 3)

def SB4():
    for i in range(15):
        addcase(10**5,10**5-1, 4)

def SB5():
    for i in range(15):
        addcase(10**5,random.randint(1, 10**5-1), 5)


SB1()
SB2()
SB3()
SB4()
SB5()
print(len(Cases))
for i in Cases:
    print(i[0],i[1],i[2])
