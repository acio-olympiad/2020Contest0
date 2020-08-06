#aux gen
Cases = []
import random

nvals = [1/10,1/4,1/2,9/10,1]
dvals = [10,15,20,100,200]
def do_subtask(subtask,max_n,max_m,max_bandwidth, use_dvals):
    m = max_m
    for i in range(len(nvals)):
        nc = nvals[i]
        n = nc * max_n
        n = min(max_n,int(n))

        if (use_dvals):
            d = dvals[i]
        else:
            d = n

        for j in nvals:
            k = j * n
            k = min(max_n,int(k))
            disconnect_starting_node = 1 if (random.randint(1,10) == 1) else 0
            high_starting_node_bandwidth = 1 if (random.randint(1,10) == 1) else 0
            for bump_k_target in range(2):
                s = f"{subtask} {max_bandwidth} {disconnect_starting_node} {high_starting_node_bandwidth} {bump_k_target} {n} {m} {k} {d}"
                Cases.append(s)

do_subtask(1,100000,100000,2,False)
do_subtask(2,100000,100000,20,False)
do_subtask(3,1000,1000,1000000,False)
do_subtask(4,100000,100000,1000000,True)

for case in Cases:
    print(case)

"""
first line: 
subtask
max_bandwidth
disconnect_starting_node - boolean, if true, starting node is disconnected (10% of cases)
high_starting_node_bandwidth - boolean, if true, starting node's bandwidth is max_bandwidth (10% of cases)
bump_k_target - boolean, if true, then once a stronger K is determined, it will increment K if possible (50% of cases)
n
m
k 
d

"""