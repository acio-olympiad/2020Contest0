import os
import random

types = ["all-blue", "all-red", "alternating", "end-biased", "middle-biased", "ascending", "3reds", "no-adjacent-reds", "random-v1", "random-v2", "random-v3", "mixed"]
block_types = [3,4,5,9,11]

def print_system(command):
    print("Generating", command.split()[-1])
    os.system(command)

def gen_case(of, sb, *args):
    print_system("python gen.py %d %s > %s-sub%d.in" % (sb, ' '.join(map(str,args)), of, sb))

def sub1():
    for i in range(16):
        print_system("python gen-sub1.py %d > %d-sub1.in" % (i,i))

def sub2():
    gen_case("min", 2, 4)
    for i in range(10):
        gen_case("small-%d" % i, 2, random.randint(6,10))
    for i in range(3):
        gen_case("random-%d" % i, 2)
    for i in range(3):
        gen_case("max-%d" % i, 2, 100000)

def sub3():
    gen_case("min", 3, 4)
    for i in range(5):
        gen_case("small-%d" % i, 3, random.randint(6,10))
    for i in range(len(types)):
        gen_case("size-999-%s" % types[i], 3, 999, i)
    for i in range(len(types)):
        gen_case("max-%s" % types[i], 3, 1000, i)
    for i in range(5):
        gen_case("max-%d" % i, 3, 1000)

    for block_count in [2,3,4,9,10,99,100,397,400]:  
        for block_type in block_types:
            gen_case("block-%d-%s" % (block_count, types[block_type]), 3, 1000, block_type, block_count)

def sub4():
    gen_case("min", 4, 4)
    for i in range(10):
        gen_case("small-%d" % i, 4, random.randint(6,10))
    for i in range(3):
        gen_case("random-%d" % i, 4)
    for i in range(3):
        gen_case("max-%d" % i, 4, 100000)

def sub5():
    gen_case("min", 5, 4)
    for i in range(10):
        gen_case("small-%d" % i, 5, random.randint(6,10))
    for i in range(len(types)):
        gen_case("size-99999-%s" % types[i], 5, 99999, i)
    for i in range(len(types)):
        gen_case("max-%s" % types[i], 5, 100000, i)
    for i in range(10):
        gen_case("max-%d" % i, 5, 100000)

    for block_count in [2,3,4,9,10,99,100,999,1000,9999,10000,39997,40000]:  
        for block_type in block_types:
            gen_case("block-%d-%s" % (block_count, types[block_type]), 5, 100000, block_type, block_count)

sub1()
sub2()
sub3()
sub4()
sub5()
