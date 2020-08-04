import random
import sys

op = int(sys.argv[1])
if op == 1:
    print(sys.argv[2], sys.argv[3])
    print(sys.argv[4], sys.argv[5])
elif op == 2:
    # Pure random, subtask 2
    print(random.randint(1, 10000), random.randint(1, 10000))
    print(1, 1)
elif op == 3:
    # Pure random, subtask 5
    l, w = random.randint(1, 10000), random.randint(1, 10000)
    print(l, w)
    print(random.randint(1, l), random.randint(1, w))
elif op == 4:
    # Small A, B random, subtask 5
    l, w = random.randint(1, 10000), random.randint(1, 10000)
    print(l, w)
    print(random.randint(1, min(10, l)), random.randint(1, min(10, w)))
