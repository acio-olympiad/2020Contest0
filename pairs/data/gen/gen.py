import sys
import random

usage = """
Usage:
To generate a random case for a subtask use:
python gen.py <subtask>
To specify additional parameters, use:
python gen.py <subtask> <N>
case will be written to stdout
subtask - the subtask of case (1-5)
N - number of beads (1 - subtask limit)
"""


SUBTASKS = 4
MAX_SKILL = int(1e5)
MIN_SKILL = 0

def random_skills(N):
    mn_skill = random.randint(MIN_SKILL,MAX_SKILL)
    mx_skill = random.randint(MIN_SKILL,MAX_SKILL)
    mn_skill,mx_skill = min(mn_skill,mx_skill),max(mn_skill,mx_skill)
    return [random.randint(mn_skill,mx_skill) for i in range(N)]

def binary_skills(N):
    return [random.randint(0,1) for i in range(N)]

def triangle_skills(N):
    return list(range(1,N+1))

def random_range(skills):
    mn = MAX_SKILL
    mx = MIN_SKILL
    for s in skills:
        mn = min(s,mn)
        mx = max(s,mx)
    a = random.randint(mn*2,mx*2)
    b = random.randint(mn*2,mx*2)
    a,b = min(a,b),max(a,b)
    return a,b

def random_a_inf_b(skills):
    mn = MAX_SKILL
    mx = MIN_SKILL
    for s in skills:
        mn = min(s,mn)
        mx = max(s,mx)
    a = random.randint(mn*2,mx*2)
    b = mx*2
    return a,b

defaults = (100000, random_range, random_skills)
subtask_info = (
    (),
    (1000, defaults[1], defaults[2]),
    (defaults[0], defaults[1], triangle_skills),
    (defaults[0], random_a_inf_b, defaults[2]),
    defaults
) # MAXN, range gen, skill gen 

args = sys.argv[1:]

if len(args) < 1:
    print(usage)
    exit(0)

subtask = int(args[0])
if subtask < 1 or subtask > SUBTASKS:
    print("Invalid subtask: '%d'. Must be between (1 - %d)" % (subtask,SUBTASKS))
    exit(0)

MAXN, range_gen, skill_gen = subtask_info[subtask]

if len(args) > 1:
    N = int(args[1])
    if N < 2 or N > MAXN:
        print("Invalid N for subtask: '%d'. Must be between (2 - %d)" % (N,MAXN))
        exit(0)
else:
    N = random.randint(2, MAXN)

skills = skill_gen(N)
A,B = range_gen(skills)
print(N,A,B)
print(*skills)
