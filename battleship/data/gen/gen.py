#aux gen
Cases = []
import random
def addcase(n,m,k,t):
    Cases.append([n,m,k,t])
    
def SB1():
    for i in [20,50,100,300,500]:
        addcase(1,1000,i,0)
        addcase(1,1000,i,1)
    addcase(1,2,1,0) #edge case

def SB2():
    for i in [200,200,200,200,200,1000,1000]:
        addcase(i,i,i,0)
        addcase(i,i,i,1)
    addcase(2,2,2,0) #edge case

def SB3to5(subtask_number):
    n = [0,0,0,30,80,200][subtask_number]
    for i in [10, 20,30,50,75,80,100,150]:
        if i > n:
            break
        for j in range(3):
            addcase(n,n - random.randint(0,5), i, random.randint(0,1))

def SB6():
    for k in [32,64,128,256,512,900]:
        addcase(1000,1000,k,0)
        addcase(1000,1000,k,1)

def disp():
    print(len(Cases))
    for i in Cases:
        print(" ".join([str(c) for c in i]))

SB1()
SB2()
SB3to5(3)
SB3to5(4)
SB3to5(5)
SB6()
disp()
        
