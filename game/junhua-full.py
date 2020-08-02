#k = open("gamein.txt","r")
#l = open("gameout.txt","w")
def read(): return(input()) #return(k.readline())
def write(x): print(x) #l.write(str(x))
[N,K]=[int(c) for c in read().split()]
A = [int(c) for c in read().split()]
B = [0]
for i in range(N):
    B.append(B[-1] + A[i])
B = (B[::-1])[:-2]
B.sort()
Ans = 0
while len(B) and B[-1] > 0 and K:
    Ans += B.pop()
    K -= 1
write(Ans)
#k.close()
#l.close()
