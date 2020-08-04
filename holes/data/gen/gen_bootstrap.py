import random
import itertools
import os

cnt = 1

def case(name, a):
    global cnt
    cmd = "python3 gen/gen.py %s > %s_%d.in" % (" ".join(map(str, a)), name, cnt)
    print(cmd)
    os.system(cmd)
    cnt += 1

# Sub1
case("AxxxxA_one", [1, 12, 8, 5, 2])

# Sub2
case("Axx11A_max", [1, 10000, 10000, 1, 1])
for i in range(8):
    case("Axx11A", [2])

for i in range(3):
    w = random.randint(1, 10000)
    case("A1x11A", [1, 1, w, 1, 1])

for i in range(5):
    l = random.randint(1, 10000)
    case("Ax111A", [1, l, 1, 1, 1])

# Sub3
for i in range(5):
    l = random.randint(1, 10000)
    ml = l
    if i >= 2:
        ml = min(ml, 100)
    a = random.randint(1, ml)
    case("Ax1x1A", [1, l, 1, a, 1])

# Sub4, includes min case
for l, w, a, b in list(filter(lambda t: t[2] <= t[0] and t[3] <= t[1] and t[1] <= t[0], itertools.product([1, 2, 3, 4, 5], repeat=4))):
    case("A%d%d%d%dA" % (l, w, a, b), [1, l, w, a, b])

# Sub5
for i in range(3):
    case("AxxxxA_rand", [3])
for i in range(5):
    case("AxxxxA_biglw", [4])
