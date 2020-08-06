import os
def r(c):
    print("[B]", c)
    os.system(c)

x = input()
cnt = 1
while x:
    r("echo %s | ./casegen > t_%d.in" % (x, cnt))
    x = input()
    cnt = cnt+1
