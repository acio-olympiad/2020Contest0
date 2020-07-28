lines = list(open("pairs.in"))

N,A,B = map(int, lines[0].split())

skills = list(map(int, lines[1:]))

skills.sort()
ans=0
l=r=N-1
for s in range(N):
    l = max(l,s)
    r = max(r,s)
    while l > s and skills[s] + skills[l] >= A:l-=1
    while r > s+1 and skills[s] + skills[r] > B:r-=1
    ans += r-l

open("pairs.out","w").write(str(ans))

