import os
import random

def print_system(command):
    print("Generating", command.split()[-1])
    os.system(command)

def gen_case(of, sb, *args):
    print_system("python gen.py %d %s > %s-sub%d.in" % (sb, ' '.join(map(str,args)), of, sb))

def sub1():
    print("Subtask 1...")
    gen_case("min", 1, 2)
    for i in range(10):
        gen_case("small-%d" % i, 1, random.randint(6,10))
    for i in range(5):
        gen_case("random-%d" % i, 1, random.randint(2,1000))
    for i in range(5):
        gen_case("max-%d" % i, 1, 1000)

def sub2():
    print("Subtask 2...")
    gen_case("min", 2, 2)
    for i in range(10):
        gen_case("small-%d" % i, 2, random.randint(6,10))
    for i in range(5):
        gen_case("random-%d" % i, 2, random.randint(2,100000))
    for i in range(5):
        gen_case("max-%d" % i, 2, 100000)

def sub3():
    print("Subtask 3...")
    gen_case("min", 3, 2)
    for i in range(10):
        gen_case("small-%d" % i, 3, random.randint(6,10))
    for i in range(5):
        gen_case("random-%d" % i, 3, random.randint(2,100000))
    for i in range(5):
        gen_case("max-%d" % i, 3, 100000)

def sub4():
    print("Subtask 4...")
    gen_case("min", 4, 2)
    for i in range(10):
        gen_case("small-%d" % i, 4, random.randint(6,10))
    for i in range(5):
        gen_case("random-%d" % i, 4, random.randint(2,100000))
    for i in range(5):
        gen_case("max-%d" % i, 4, 100000)

def sub5():
    print("Subtask 5...")
    gen_case("min", 5, 2)
    for i in range(10):
        gen_case("small-%d" % i, 5, random.randint(6,10))
    for i in range(5):
        gen_case("random-%d" % i, 5, random.randint(2,100000))
    for i in range(5):
        gen_case("max-%d" % i, 5, 100000)

sub1()
sub2()
sub3()
sub4()
sub5()
