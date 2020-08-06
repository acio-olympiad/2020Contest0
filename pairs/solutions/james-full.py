import sys

X,Y = list(sys.stdin)

N,A,B = map(int, X.split())
skills = list(map(int, Y.split()))

skills.sort()
ans=0
l=r=N-1
for s in range(N):
    l = max(l,s)
    r = max(r,s)
    while l > s and skills[s] + skills[l] >= A:l-=1
    while r > s and skills[s] + skills[r] > B:r-=1
    ans += r-l

sys.stdout.write(str(ans))

