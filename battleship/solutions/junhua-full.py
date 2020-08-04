#k = open("shipin.txt","r")
#l = open("shipout.txt","w")
def read(): return(input()) #return(k.readline())
def write(x): print(x) #l.write(str(x))

[N,M,K]=[int(c) for c in read().split()] #read input and 1 index gri
A=[[0]*(M+2)]
for i in range(N):
    Row = [int(c) for c in read().split()]
    Row.insert(0,0)
    Row.append(0)
    A.append(Row)
A.append([0]*(M+2))
    

Hsum=[]
Vsum=[[0]*(M+2)]
dp1=[[0]*(M+2) for i in range(N+2)]
dp2=[[0]*(M+2) for i in range(N+2)]

for r in range(N+2): #precalc prefix sums
    Hsum.append([0])
    for c in range(1,M+2):
        Hsum[r].append(Hsum[r][c-1]+A[r][c])
        
for r in range(1,N+2):
    Vsum.append([0])
    for c in range(1,M+2):
        Vsum[r].append(Vsum[r-1][c]+A[r][c]) 

for r in range(1,N+1): #precalculate optimums for subgrids
    for c in range(1,M+1): 
        dp1[r][c]=max(dp1[r-1][c],dp1[r][c-1])
        if r >= K:
            dp1[r][c]=max(dp1[r][c], Vsum[r][c] - Vsum[r-K][c])
        if c >= K:
            dp1[r][c]=max(dp1[r][c], Hsum[r][c] - Hsum[r][c-K])

for r in range(N,0,-1):
    for c in range(M,0,-1):
        dp2[r][c]=max(dp2[r+1][c],dp2[r][c+1])
        if r+K-1 <= N:
            dp2[r][c]=max(dp2[r][c], Vsum[r+K-1][c] - Vsum[r-1][c])
        if c+K-1 <= M:
            dp2[r][c]=max(dp2[r][c], Hsum[r][c+K-1] - Hsum[r][c-1])

Ans = 0 #calculate Answer
for r in range(1,N): #split at row: 1 ... i is one, i+1 ... N is other
    Ans = max(Ans, dp1[r][M] + dp2[r+1][1])
for c in range(1,M): #split at column: 1 ... i is one, i+1 ... M is other
    Ans = max(Ans, dp1[N][c] + dp2[1][c+1])

write(Ans)


#k.close()
#l.close()

