import sys
input = lambda : sys.stdin.readline().rstrip()

from collections import Counter

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    M = max(a)
    a.sort()
    a.pop()

    aOptimal = [M]
    aResidue = []
    seen = set([M])

    # Creating optimal order
    for num in a:
        if num not in seen: aOptimal.append(num)
        else: aResidue.append(num)
        seen.add(num)
    aOptimal += aResidue

    # Finding value
    value = n*M

    seen = set()
    mex = 0
    for num in aOptimal:
        seen.add(num)
        while mex in seen: mex += 1
        value += mex
    print(value)    

t = int(input())
for _ in range(t): solve()
