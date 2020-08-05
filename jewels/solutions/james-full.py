import sys

N,jewels = sys.stdin
jewels = jewels.strip()

blocks = []
l = 0
c = jewels[0] 
for j in jewels:
    if j == c:
        l += 1
    else:
        blocks.append((l,c))
        c = j
        l = 1
blocks.append((l,c))

#print(blocks)

ans = 0
if len(blocks) > 1:
    if blocks[-1][1] == blocks[0][1]:
        l,c = blocks[0]
        l += blocks[-1][0]
        blocks[-1] = (l,c)
        blocks[0] = (l,c)
    else:
        ans = blocks[0][0] + blocks[-1][0]
    s = blocks[0][0]
    for i in range(1,len(blocks)):
        s += blocks[i][0]
        ans = max(ans,s)
        s -= blocks[i-1][0]
else:
    ans = N

sys.stdout.write(str(ans) + "\n")
