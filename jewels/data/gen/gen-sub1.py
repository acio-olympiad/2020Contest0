import sys

t = int(sys.argv[1])

s = []
for i in range(4):
    if t & (1<<i):
        s.append('r')
    else:
        s.append('b')

print(4)
print(''.join(s))
