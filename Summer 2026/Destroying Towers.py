import sys
input = lambda : sys.stdin.readline().rstrip()

from math import inf

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    m = inf
    total = 0

    for height in a:
        m = min(height, m)
        total += m
    print(total)

t = int(input())
for _ in range(t): solve()
