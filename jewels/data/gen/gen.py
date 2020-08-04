import sys
import random

usage = """
Usage:
To generate a random case for a subtask use:
python gen.py <subtask>
To specify additional parameters, use:
python gen.py <subtask> <N> <casetype> <arg1> <arg2> ...
case will be written to stdout
subtask - the subtask of case (1-5)
N - number of beads (1 - subtask limit)
casetype - the type of case to be generated (0-11)
arg - argument to pass to casetype
"""

def random_partition(cnt, n=0): # O(n)
    if n == 0:
        n = random.randint(1,max(1,cnt))
    if cnt == 0:
        return [0] * n
    density = [random.uniform(0.0, 1.0)for i in range(n)]
    mul = cnt/sum(density)

    split = [int(mul * d) for d in density]
    delta = sum(split)-cnt

    while delta < 0:
        idx = random.randrange(0,n)
        split[idx] += 1
        delta += 1

    return split

def blocks_to_string(blocks):
    s = []
    for b in range(len(blocks)):
        s.append(("rb"[b%2])*blocks[b]) #maybe make blue first 50% of the time?
    return ''.join(s)

def blue(N):
    return 'b'*N

def red(N):
    return 'r'*N

def alternating(N):
    s = []
    for i in range(N):
        s.append("rb"[i%2])
    return ''.join(s)

def end_biased(N, B=0):
    blocks = random_partition(N,B)
    blocks.sort()
    biased = []
    for i in range(len(blocks)-1, -1, -2):
        biased.append(blocks[i])
    for i in range(len(blocks)%2, len(blocks), 2):
        biased.append(blocks[i])    
    return blocks_to_string(biased)

def middle_biased(N, B=0):
    blocks = random_partition(N,B)
    blocks.sort()
    biased = []
    for i in range(0, len(blocks), 2):
        biased.append(blocks[i])
    for i in range(len(blocks)-1-len(blocks)%2, -1, -2):
        biased.append(blocks[i])    
    return blocks_to_string(biased)

def ascending(N, B=0):
    blocks = random_partition(N,B)
    blocks.sort()
    return blocks_to_string(blocks)

"""
def sub2(N): # at most 3 red
    reds = random.randint(0, min(N,3))
    s = blue(N-reds)
    for i in range(reds):
        split = random.randint(0,len(s))
        s = s[:split] + 'r' + s[split:]
    return s
"""

def random_rotate(s):
    split = random.randrange(0,len(s))
    return s[split:] + s[:split]

def sub2(N): # exactly 2, non adjacent reds
    assert(N >= 4)
    split = random.randint(1,N-3)
    if random.randrange(0,2):
        return 'r' + blue(split) + 'r' + blue(N-split-2)
    else:
        return blue(split) + 'r' + blue(N-split-2) + 'r'
 
def sub4(N): # no adjacent red
    reds = random.randint(0,N//2)
    if reds == 0:
        return blue(N)
    else:
        flip = random.randrange(0,1)
        blocks = random_partition(N-reds*2,reds) # need to make sure each block has at least 1 blue
        s = []
        for i in range(reds):
            if flip:
                s.append('r')
                s.append(blue(blocks[i] + 1))
            else:
                s.append(blue(blocks[i] + 1))
                s.append('r')
    return ''.join(s)

def rand(N):
    return ''.join([random.choice("rb")for i in range(N)])

def random_blocks(N, B=0):
    blocks = random_partition(N,B)
    return blocks_to_string(blocks)

def random_type(N):
    f = random.choice(CASE_TYPES)
    if f == sub2 and N < 4: # cannot gen a sub2 case with size < 4
        f = red
    return f(N)

def mixed(N, B=2):
    blocks = random_partition(N,B)
    s = [random_type(blocks[i]) for i in range(B)]
    return ''.join(s)

CASE_TYPES = [blue, red, alternating, end_biased, middle_biased, ascending, sub2, sub4, rand, random_blocks, random_type, mixed]

SUBTASKS = 5
args = sys.argv[1:]

if len(args) < 1:
    print(usage)
    exit(0)

defaults = (100000, list(range(len(CASE_TYPES))))
subtask_info = (
    (),
    (4, defaults[1]),
    (defaults[0], [6]),
    (1000, defaults[1]),
    (defaults[0], [7]),
    defaults
) # MAXN, ALLOWED CASES 

subtask = int(args[0])
if subtask < 1 or subtask > SUBTASKS:
    print("Invalid subtask: '%d'. Must be between (1 - %d)" % (subtask,SUBTASKS))
    exit(0)

MAXN, allowed_cases = subtask_info[subtask]

if len(args) > 1:
    N = int(args[1])
    if N < 4 or N > MAXN:
        print("Invalid N for subtask: '%d'. Must be between (4 - %d)" % (N,MAXN))
        exit(0)
else:
    N = random.randint(4, MAXN)

if len(args) > 2:
    case_type = int(args[2])
    if case_type not in allowed_cases:
        print("Invalid case_type for subtask: '%d'." % case_type)
        exit(0)
else:
    case_type = random.choice(allowed_cases)

print(N)
s = CASE_TYPES[case_type](N, *map(int,args[3:]))
if random.randrange(0,2):
    s = random_rotate(s)
print(s)
