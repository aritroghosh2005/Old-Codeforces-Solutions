import sys
input = lambda : sys.stdin.readline().rstrip()

from collections import deque

def solve():
    n = int(input())

    block1 = list(range(1, n+1))
    block2 = block1.copy()
    block4 = block2.copy()

    block3 = deque(block1.copy())
    block3.rotate()

    block = block1 + block2 + list(block3) + block4
    print(*block)

t = int(input())
for _ in range(t): solve()
