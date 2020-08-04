import os
cases = int(input())
cnt = 1

def r(cmd):
    print("[B]", cmd)
    os.system(cmd)

for _ in range(cases):
    ln = input()
    r("echo %s | ./tkgen > battleship%d.in" % (ln, cnt)) 
    cnt += 1

