from math import gcd
from functools import reduce

def findX(n, a):
    g = reduce(gcd, a)

    if 1 in a: return 2
    for x in range(2, max(a)+2):
        if gcd(g,x)==1: return x
    return -1  

N = int(input())
tests = []

for _ in range(N):
    n = int(input())
    a = list(map(int, input().split()))
    tests.append([n,a])

for _ in range(N):
    print(findX(tests[_][0], tests[_][1]))