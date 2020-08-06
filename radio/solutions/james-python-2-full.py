N,M,K,D = map(int,input().split())
B = [0] + list(map(int, input().split()))
G = [[] for _ in range(N+1)]
for i in range(M):
    u,v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)

def can_do(L):
    todo = [1]*(N+1)
    bfsc=bfsn=[]
    cnt = 0
    if B[1] >= L:
        todo[1]=0
        bfsn.append(1)
        cnt += 1
    for i in range(D):
        bfsc=bfsn
        bfsn=[]
        for u in bfsc:
            for v in G[u]:
                if todo[v] and B[v] >= L:
                    todo[v]=0
                    bfsn.append(v)
                    cnt += 1
    return cnt >= K

lo=mid=1
hi=1<<20
while lo!=hi:
    mid=hi+lo>>1
    if can_do(mid):
        lo = mid + 1
    else:
        hi = mid
print(lo-1)
